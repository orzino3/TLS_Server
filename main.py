from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
import numpy as np
import time
import json
import base64
import random
from datetime import datetime
from sklearn.ensemble import IsolationForest
from Crypto.Cipher import AES
from pydantic import BaseModel

app = FastAPI(title="Smart Traffic Light Security API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = b'SixteenByteKey!!'
CONFIDENCE_THRESHOLD = 85.0


def init_db():
    conn = sqlite3.connect('traffic_security.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sensor_id TEXT,
            event_type TEXT,
            risk_score REAL,
            status TEXT,
            car_count INTEGER
        )
    ''')
    conn.commit()
    conn.close()


normal_data = np.random.randint(5, 40, size=(100, 1))
ai_model = IsolationForest(contamination=0.05, random_state=42)
ai_model.fit(normal_data)


def decrypt_packet(ciphertext_b64, nonce_b64, tag_b64):
    try:
        ciphertext = base64.b64decode(ciphertext_b64)
        nonce = base64.b64decode(nonce_b64)
        tag = base64.b64decode(tag_b64)
        cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
        plain_text = cipher.decrypt_and_verify(ciphertext, tag)
        return json.loads(plain_text.decode('utf-8'))
    except:
        return None


class PacketInput(BaseModel):
    ciphertext: str
    nonce: str
    tag: str
    simulation_mode: str


@app.get("/api/logs")
def get_logs():
    conn = sqlite3.connect('traffic_security.db')
    df = pd.read_sql_query("SELECT * FROM event_logs ORDER BY id DESC LIMIT 20", conn)
    conn.close()
    return df.to_dict(orient="records")


@app.post("/api/inject")
def inject_packet(packet: PacketInput):
    payload = decrypt_packet(packet.ciphertext, packet.nonce, packet.tag)

    if not payload:
        conn = sqlite3.connect('traffic_security.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO event_logs (timestamp, sensor_id, event_type, risk_score, status, car_count) VALUES (?, ?, ?, ?, ?, ?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "UNKNOWN", packet.simulation_mode, 100.0,
             "נחסם - שגיאת פענוח", 0))
        conn.commit()
        conn.close()
        return {"status": "FAIL-SAFE_ACTIVE", "risk_score": 100.0, "reason": "Decryption / Tag Verification Failed"}

    car_count = payload.get('car_count', 0)
    sensor_id = payload.get('sensor_id', 'UNKNOWN')

    pred = ai_model.predict([[car_count]])[0]

    if pred == 1 and car_count <= 50:
        risk_score = float(np.clip(20 + (car_count * 0.5), 0, 45))
        status = "מאושר ואדפטיבי"
    else:
        if packet.simulation_mode in ["spoofing", "dos"] or car_count > 100 or car_count < 0:
            risk_score = float(np.clip(75 + (car_count * 0.4), 88.0, 100.0))
        else:
            risk_score = float(np.clip(50 + (car_count * 0.3), 50, 84.0))

        status = "הופעל Fail-Safe" if risk_score >= CONFIDENCE_THRESHOLD else "מאושר עם חריגה קלה"

    conn = sqlite3.connect('traffic_security.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event_logs (timestamp, sensor_id, event_type, risk_score, status, car_count) VALUES (?, ?, ?, ?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sensor_id, packet.simulation_mode, risk_score, status, car_count))
    conn.commit()
    conn.close()

    return {
        "status": "FAIL-SAFE_ACTIVE" if risk_score >= CONFIDENCE_THRESHOLD else "ADAPTIVE_ACTIVE",
        "risk_score": risk_score,
        "car_count": car_count,
        "calculated_green_light": int(np.clip(car_count * 1.5, 10, 60))
    }


@app.get("/api/generate-mock/{mode}")
def generate_mock_data(mode: str):
    sensors = ["SENSOR_NORTH_01", "SENSOR_SOUTH_01", "SENSOR_EAST_01", "SENSOR_WEST_01"]
    chosen_sensor = random.choice(sensors)

    if mode == "normal":
        current_time_factor = time.time()
        base_cars = 18
        wave = int(np.sin(current_time_factor / 8) * 14)
        car_count = int(max(2, base_cars + wave))
    elif mode == "spoofing":
        car_count = int(np.random.randint(140, 260))
    else:
        car_count = 999

    plain_dict = {
        "sensor_id": chosen_sensor,
        "car_count": car_count,
        "timestamp": time.time()
    }

    plain_text = json.dumps(plain_dict).encode('utf-8')
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text)

    return {
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8'),
        "nonce": base64.b64encode(cipher.nonce).decode('utf-8'),
        "tag": base64.b64encode(tag).decode('utf-8'),
        "simulation_mode": mode
    }


if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)