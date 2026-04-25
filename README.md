# 🧠 Essay AI Agent

An AI-powered essay generation and review web application built using Flask and SQLite. This project allows users to generate essays from prompts, receive feedback, and track their writing history.

---

## 🚀 Features

* ✍️ Generate essays from user prompts
* 📊 Automatic scoring system (out of 10)
* 🧾 Feedback suggestions for improvement
* 🔐 Simple login system (email-based)
* 📁 Essay history tracking per user
* 📉 Basic plagiarism estimation

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite
* **Frontend:** HTML (Templates)
* **API:** REST endpoints

---

## 📂 Project Structure

```
ESSAYAIAGENTPRJ/
│
├── app.py              # Main Flask application
├── run.py              # App runner
├── users.db            # SQLite database
├── essays.db           # Essay storage (if separate)
├── templates/          # HTML pages
├── .env                # Environment variables (not uploaded)
├── .venv/              # Virtual environment (not uploaded)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/essayaiagent.git
cd essayaiagent
```

2. Create virtual environment:

```
python -m venv .venv
```

3. Activate it:

* Windows:

```
.venv\Scripts\activate
```

* Mac/Linux:

```
source .venv/bin/activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the App

```
python app.py
```

Then open:

```
http://127.0.0.1:5000/
```

---

## 🔑 API Endpoints

### Login / Signup

```
POST /login-api
```

### Generate Essay

```
POST /generate
```

### View History

```
GET /history/<email>
```

---

## 📊 How Scoring Works

* Starts from **10 points**
* Deducts points if:

  * Prompt is too short
  * Lacks personal voice ("I")
* Minimum score: **4/10**

---

## ⚠️ Important Notes

* `.env` file is not included for security reasons
* `.venv/` should not be uploaded to GitHub
* This is a basic AI simulation (not using real AI APIs yet)

---

## 🌟 Future Improvements

* Integrate real AI APIs (like OpenAI)
* Add authentication with passwords hashing
* Improve plagiarism detection
* Enhance UI/UX
* Add essay editing and export options

---

## 👩‍💻 Author

Tanvi Jadhav

---

## 📄 License

This project is for educational purposes.
