from flask import Flask, render_template, request, redirect, Response
from twilio.rest import Client
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
import re
import httpx

load_dotenv()
app = Flask(__name__)

# Twilio setup
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
FROM_NUMBER = os.getenv("TWILIO_PHONE")

# DB setup
DB = "calls.db"
conn = sqlite3.connect(DB)
conn.execute("CREATE TABLE IF NOT EXISTS calls (number TEXT, status TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")
conn.close()

def log_call(number, status):
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO calls VALUES (?, ?)", (number, status))
    conn.commit()
    conn.close()

def make_call(number):
    try:
        call = client.calls.create(
            to=number,
            from_=FROM_NUMBER,
            url="http://127.0.0.1:5000/voice.xml"
        )
        log_call(number, "called")
    except Exception as e:
        log_call(number, f"failed: {str(e)}")

def generate_article(title):
    prompt = f"Write a detailed, engaging blog article on the topic: '{title}'. Include examples and explanations."

    headers = {
        "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-reasoning",  # You can also try "pplx-70b-chat"
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that writes technical blog articles."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = httpx.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers, timeout=80)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        return f"Failed to generate article: {e.response.text}"
    except Exception as e:
        return f"Failed to generate article: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numbers = request.form["numbers"].splitlines()
        for num in numbers:
            make_call(num.strip())
        return redirect("/")
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def prompt():
    text = request.form["prompt"]
    match = re.search(r"call (\+?\d{10,})", text.lower())
    if match:
        number = match.group(1)
        if not number.startswith("+"):
            number = "+91" + number
        make_call(number)
    return redirect("/")

@app.route("/log")
def log():
    df = pd.read_sql("SELECT * FROM calls", sqlite3.connect(DB))
    return df.to_html(classes="table table-bordered")

@app.route("/voice.xml")
def voice():
    message = "Hello, this is Autodialer AI. Your appointment is confirmed. Have a great day."
    twiml = f"""
    <Response>
        <Say voice="Polly.Joanna" language="en-IN">{message}</Say>
    </Response>
    """
    return Response(twiml, mimetype='text/xml')

@app.route("/blog")
def blog():
    conn = sqlite3.connect(DB)
    posts = conn.execute("SELECT title, content FROM blog ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("blog.html", posts=posts)

@app.route("/generate_blog", methods=["POST"])
def generate_blog():
    titles = request.form["titles"].splitlines()
    for title in titles:
        content = generate_article(title.strip())
        conn = sqlite3.connect(DB)
        conn.execute("INSERT INTO blog (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        conn.close()
    return redirect("/blog")

if __name__ == "__main__":
    app.run(debug=True)
