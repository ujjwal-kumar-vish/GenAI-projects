from flask import Flask, render_template, request, redirect
from twilio.rest import Client
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
import re

load_dotenv()
app = Flask(__name__)

# Twilio setup
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
FROM_NUMBER = os.getenv("TWILIO_PHONE")

# DB setup
DB = "calls.db"
if not os.path.exists(DB):
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE calls (number TEXT, status TEXT)")
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
            url="http://demo.twilio.com/docs/voice.xml"
        )
        log_call(number, "called")
    except Exception as e:
        log_call(number, f"failed: {str(e)}")

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
    match = re.search(r"call (\d{10,})", text)
    if match:
        number = "+91" + match.group(1)
        make_call(number)
    return redirect("/")

@app.route("/log")
def log():
    df = pd.read_sql("SELECT * FROM calls", sqlite3.connect(DB))
    return df.to_html(classes="table table-bordered")

if __name__ == "__main__":
    app.run(debug=True)
