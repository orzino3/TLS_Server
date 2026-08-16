# 🛡️ Smart Traffic Light Security API (Backend)

מערכת Backend מבוססת **FastAPI** המשמשת כלבת האבטחה, ההצפנה וניתוח האנומליות (AI) של פרויקט הגמר **TLS (Traffic Light Security)**. השרת אחראי על קבלת חבילות נתונים מחיישני הקצה, פענוח קריפטוגרפי, הפעלת מודל למידת מכונה לזיהוי מתקפות (Spoofing / DoS) ותיעוד פורנזי במסד נתונים מקומי.

---

## 🚀 טכנולוגיות וכלים
* **Python 3.10+**
* **FastAPI & Uvicorn** (בניית ה-API וניהול השרת)
* **PyCryptodome** (הצפנה מאומתת AES-256 במצב EAX)
* **scikit-learn** (מודל Isolation Forest לזיהוי אנומליות)
* **SQLite & Pandas** (ניהול ושליפת לוגים ממוסדים)

---

## 📂 מבנה פרויקט השרת
```text
backend/
│
├── main.py               # קובץ השרת הראשי (Endpoints, Crypto, AI Engine)
├── traffic_security.db   # מסד הנתונים של אירועי הסייבר והתנועה (נוצר אוטומטית)
└── requirements.md / txt # תלויות המערכת
