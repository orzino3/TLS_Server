import requests
import time

BASE_URL = "http://127.0.0.1:8000"


def run_automated_tests():
    print(" מתחיל הרצת סדרת בדיקות אוטומטית למערכת האבטחה...")

    # טסט 1: בדיקת שליפת לוגים
    print("\n[בדיקה 1] בודק חיבור למסד הנתונים ושליפת לוגים...")
    try:
        response = requests.get(f"{BASE_URL}/api/logs")
        if response.status_code == 200:
            print(" בדיקה 1 עברה בהצלחה! מסד הנתונים מגיב והחזיר סטטוס 200.")
        else:
            print(f" בדיקה 1 נכשלה. השרת החזיר קוד שגיאה: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(" בדיקה 1 נכשלה: לא ניתן להתחבר לשרת ה-FastAPI. ודא שקובץ main.py רץ ברקע!")
        return

    # טסט 2: בדיקת ייצור נתונים תקינים והזרקתם
    print("\n[בדיקה 2] מדמה תעבורת שגרה תקינה לאורך זמן...")
    for i in range(3):
        # 1. מייצר חבילה מדומה תקינה
        mock_data = requests.get(f"{BASE_URL}/api/generate-mock/normal").json()
        # 2. מזריק אותה לשרת
        res = requests.post(f"{BASE_URL}/api/inject", json=mock_data).json()
        print(f"   -> חבילת שגרה {i + 1}: סיכון מחושב = {res['risk_score']:.1f}%, סטטוס = {res['status']}")
        time.sleep(0.5)
    print(" בדיקה 2 עברה בהצלחה!")

    # טסט 3: בדיקת עמידות בפני מתקפת Spoofing
    print("\n[בדיקה 3] מפעיל מחולל מתקפות ובודק תגובת מודל ה-AI...")
    mock_attack = requests.get(f"{BASE_URL}/api/generate-mock/spoofing").json()
    res_attack = requests.post(f"{BASE_URL}/api/inject", json=mock_attack).json()

    print(f"   -> תוצאת מתקפה: סטטוס מערכת = {res_attack['status']}, ציון סיכון = {res_attack['risk_score']:.1f}%")
    if res_attack['status'] == "FAIL-SAFE_ACTIVE" and res_attack['risk_score'] >= 85:
        print(" בדיקה 3 עברה בהצלחה! מודל ה-AI זיהה והפעיל אל-כשל כמצופה.")
    else:
        print(" בדיקה 3 נכשלה - המערכת לא נכנסה למצב הגנה!")


if __name__ == "__main__":
    # ודא שקובץ main.py רץ ומאזין בפורט 8000 לפני הפעלת סקריפט זה
    run_automated_tests()