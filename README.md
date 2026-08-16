🛡️ TLS - Traffic Light Security (Backend Service)

מנוע עיבוד קצה (Edge Backend Engine) המבוסס על FastAPI, SQLite, הצפנה קריפטוגרפית (AES-256 EAX) ומודל בינה מלאכותית (Isolation Forest) לניתוח בזמן אמת של תשדורות חיישנים וזיהוי מתקפות סייבר בצומת רמזורים חכם.

📐 ארכיטקטורה וטכנולוגיות

שפה ופלטפורמה: Python 3.10+

שרת אינטרנט ו-API: FastAPI + Uvicorn (Asynchronous ASGI)

אימות וקריפטוגרפיה: PyCryptodome (AES-256 בשיטת EAX Mode לביצוע הצפנה מאומתת ואימות שלמות)

מודל AI & Anomaly Detection: Scikit-Learn (אלגוריתם Isolation Forest לא-מפוקח)

מסד נתונים פורנזי: SQLite 3 (traffic_security.db)

עיבוד נתונים: Pandas & NumPy

⚙️ רכיבי הליבה בשרת

CryptoEngine (פענוח ואימות שלמות):

פענוח חבילות מוצפנות ב-Base64.

אימות קוד ה-Tag הקריפטוגרפי. חבלה בביט בודד תכשיל את הפענוח ותקבע 100% סיכון (חסימה מיידית).

AIEngine (זיהוי אנומליות נפח תנועה):

מודל Isolation Forest המאומן בזיכרון על ערכי שגרה (5–40 רכבים).

סיווג אנומליות וחישוב ציון סיכון (Risk Score) רציף בטווח של 0.0% עד 100.0%.

Fail-Safe Logic (מנגנון אל-כשל):

השוואת ציון הסיכון מול סף הרגישות (CONFIDENCE_THRESHOLD = 85%).

החזרת הוראת FAIL-SAFE_ACTIVE במידה והסיכון עבר את הסף או שהפענוח נכשל.

SQLite Logger (יומן אירועים):

רישום קשיח של כל האירועים והניתוחים לטבלה event_logs.

📡 נתיבי תקשורת (API Endpoints)

שיטה

נתיב

תיאור

GET

/api/logs

שליפת 20 אירועי הסייבר והתנועה האחרונים מ-SQLite עבור ה-Dashboard

POST

/api/inject

קבלת חבילה מוצפנת, פענוח קריפטוגרפי, אימות AI, חישוב ירוק/Fail-Safe ורישום ל-DB

GET

/api/generate-mock/{mode}

מחולל סימולציות המצפין חבילה מדומה לפי מצב (normal, spoofing, dos)

GET

/docs

ממשק תיעוד אינטראקטיבי מובנה (Swagger UI)

🚀 הוראות התקנה והרצה

1. דרישות קדם

Python 3.10 ומעלה מותקן במחשב.

2. התקנת תלויות (Dependencies)

פתחו את ה-Terminal בתיקיית ה-Backend והריצו:

pip install fastapi uvicorn pycryptodome scikit-learn pandas numpy


3. הפעלת השרת

הריצו את הקובץ המרכזי:

python main.py


לחלופין, ניתן להריץ דרך Uvicorn במידה ומשנים פרמטרים:

uvicorn main:app --reload --host 127.0.0.1 --port 8000


השרת יעלה בכתובת: http://127.0.0.1:8000

ממשק ה-Swagger יהיה זמין בכתובת: http://127.0.0.1:8000/docs

📂 מבנה מסד הנתונים (traffic_security.db)

הטבלה event_logs כוללת את השדות הבאים:

id (INTEGER, Primary Key Auto-Increment)

timestamp (TEXT, YYYY-MM-DD HH:MM:SS)

sensor_id (TEXT, למשל SENSOR_NORTH_01)

event_type (TEXT, normal / spoofing / dos)

risk_score (REAL, 0.0 - 100.0)

status (TEXT, סטטוס ההגנה שנרשם)

car_count (INTEGER, כמות הרכבים שנפלטה מהפענוח)
