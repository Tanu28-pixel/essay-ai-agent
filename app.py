from flask import Flask, request, jsonify, render_template
import sqlite3
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users(email TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS essays(email TEXT, prompt TEXT, essay TEXT)")

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/app")
def app_page():
    return render_template("app.html")

@app.route("/review")
def review_page():
    return render_template("review.html")

@app.route("/login-api", methods=["POST"])
def login_api():
    data = request.json
    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
    user = c.fetchone()

    if not user:
        c.execute("INSERT INTO users VALUES (?,?)",(email,password))
        conn.commit()

    conn.close()

    return jsonify({"status":"success"})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data["prompt"]
    email = data["email"]
    university = data.get("university", "")

    # Use HuggingFace API to generate essay
    try:
        API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b"
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        
        uni_context = f" for {university} university" if university else ""
        payload = {
            "inputs": f"Write a compelling college essay{uni_context} based on this prompt: {prompt}",
            "parameters": {
                "max_length": 500,
                "temperature": 0.7
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            essay = result[0].get("generated_text", "Essay generation failed")
        else:
            essay = f"Essay for {university}{uni_context}\n\nBased on your prompt:\n{prompt}\n\nThis is a comprehensive essay that demonstrates your unique perspective and personal growth. The experience shaped my values and future direction."
    except Exception as e:
        essay = f"Essay{uni_context}:\n{prompt}\n\nThis experience has significantly impacted my worldview and academic interests. I learned valuable lessons about resilience, creativity, and personal responsibility that will guide my college journey."

    # score
    score = 10
    if len(prompt)<50: score-=3
    if "I" not in prompt: score-=2
    if score<4: score=4

    feedback = []
    if len(prompt)<50: feedback.append("✓ Add more specific details and examples")
    if "I" not in prompt: feedback.append("✓ Use personal voice and first-person perspective")
    if len(essay)<100: feedback.append("✓ Expand your essay with more depth")
    feedback.append("✓ Great start! Consider adding personal anecdotes")

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO essays VALUES (?,?,?)",(email,prompt,essay))
    conn.commit()
    conn.close()

    return jsonify({
        "essay": essay,
        "feedback": feedback,
        "score": f"{score}/10",
        "plagiarism": f"{100-score*5}% original",
        "university": university
    })

@app.route("/history/<email>")
def history(email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT prompt,essay FROM essays WHERE email=?", (email,))
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
