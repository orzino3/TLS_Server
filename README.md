# 🛡️ Traffic Light Security API (Backend)

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
```

---

## ⚙️ התקנה והרצה

1. **שיבוט המאגר והתחברות לתיקייה:**
   ```bash
   cd backend
   ```

2. **התקנת הספריות הנדרשות:**
   ```bash
   pip install fastapi uvicorn pycryptodome scikit-learn pandas numpy pydantic
   ```

3. **הפעלת השרת (עם Hot-Reload):**
   ```bash
   python main.py
   # או לחלופין:
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```
   השרת ירוץ בכתובת: \`http://127.0.0.1:8000\`

---

## 🔌 API Endpoints עיקריים

| מתודה | נתיב | תיאור קצר |
| :--- | :--- | :--- |
| **GET** | \`/api/logs\` | מחזיר את 20 האירועים האחרונים ממסד הנתונים (ממוינים לפי ID יורד). |
| **POST** | \`/api/inject\` | מקבל חבילה מוצפנת, מפענח, מריץ בדיקת AI, מעדכן DB ומחזיר סטטוס Fail-Safe / Adaptive. |
| **GET** | \`/api/generate-mock/{mode}\` | מייצר חבילה סימולטיבית מוצפנת לפי מצב (\`normal\`, \`spoofing\`, \`dos\`). |
`;

    const frontendContent = `# 🚦 Smart Traffic Light Security Dashboard (Frontend)

ממשק ניהול ובקרה ויזואלי (**Dashboard**) המפותח ב-**React / Next.js**, המציג בזמן אמת את זרימת התנועה בצומת, מפת חיישנים פיזיקלית, יומן אירועי סייבר פורנזי, ומדדי סיכון מבוססי AI.

---

## 🚀 טכנולוגיות וכלים
* **Next.js 14+ (App Router)** & **React**
* **TypeScript** (אכיפת טיפוסים קשיחה)
* **Tailwind CSS** (עיצוב מודרני מותאם למצב כהה / Cyber Theme)
* **Lucide React** (אייקונים הנדסיים ונקיים)
* **HTML5 Canvas / SVG** (אנימציית זרימת הרכב והרמזורים בצומת)

---

## 📂 מבנה פרויקט הלקוח
```text
frontend/
│
├── app/
│   ├── page.tsx          # המסך הראשי הכולל את ה-Dashboard והלוגיקה
│   └── layout.tsx        # מעטפת היישום והגדרות גלובליות
├── components/           # רכיבי UI (כפתורים, כרטיסיות, טבלאות)
└── public/               # קבצים סטטיים ואסאטים
```

---

## ⚙️ התקנה והרצה

1. **התחברות לתיקיית הלקוח:**
   ```bash
   cd frontend
   ```

2. **התקנת חבילות וספריות (NPM / Yarn):**
   ````bash
   npm install
   # לחלופין:
   yarn install
   ```

3. **הפעלת שרת פיתוח מקומי:**
   ```bash
   npm run dev
   # לחלופין:
   yarn dev
   ```
   ה-Dashboard יהיה זמין בכתובת: \`http://localhost:3000\`

---

## 🎯 יכולות מרכזיות בממשק
* **מפת צומת דינמית:** הדמיה פיזיקלית של רכבים הנעים ב-4 כיוונים (צפון, דרום, מזרח, מערב) בהתאם למצבי הרמזורים.
* **יומן אירועים פורנזי (SQLite Sync):** טבלה חיה המציגה את כלל השידורים, רמות הסיכון, וסטטוס ההגנה (מאושר / נחסם).
* **כפתורי סימולציה מהירים:** הזרקת מידע בשגרה, הדמיית התקפת Spoofing, והצפת DoS לבחינת תגובת המערכת בזמן אמת.
* **מסך הגדרות וכיול:** שינוי רגישות מודל ה-AI (\`Confidence Threshold\`) והגדרת מצבי אל-כשל (\`Fail-Safe\`).
`
