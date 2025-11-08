# Autodialer

Small Flask demo that places outbound calls using Twilio and logs call attempts to a local SQLite database.

This README explains how to set up and run the Autodialer project locally (Linux). The instructions assume you are on the `Autodialer` branch or working on that folder.

## What it does
- Web UI at `/` where you can paste phone numbers (one per line) to place calls.
- A `/prompt` endpoint accepts a textual prompt and will trigger a call if it matches `call <number>`.
- Call attempts and results are stored in `calls.db` (SQLite) in the same folder.

The main behavior is implemented in `main.py` which uses Flask, Twilio, pandas and sqlite3.

## Requirements
- Python 3.8+
- See `req.txt` for the exact Python dependencies used by this project.

## Environment variables
Create a `.env` file in the `Autodialer/` folder (or set these variables in your environment). Example `.env`:

```
TWILIO_SID=your_twilio_account_sid
TWILIO_TOKEN=your_twilio_auth_token
TWILIO_PHONE=+1234567890   # the Twilio phone number you'll send calls from
```

Important: Keep these secrets private. Do not commit `.env` to the repository. Consider adding it to `.gitignore`.

## Quick start (Linux)
1. Create and activate a virtual environment

```bash
cd Autodialer
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r req.txt
```

3. Create `.env` with your Twilio credentials (see above)

4. Run the app

```bash
python main.py
```

The Flask app will start on http://127.0.0.1:5000 by default. Open that URL in your browser.

## Database / logs
- A file named `calls.db` will be created automatically in the `Autodialer/` folder on first run. It contains a `calls` table with columns `(number, status)`.

To inspect logs quickly you can use the `/log` endpoint in the running app which returns an HTML table produced by pandas.

## Testing and safety
- Twilio calls may incur costs. Use test credentials or Twilio's testing/sandbox features if you want to avoid real calls.
- Validate phone numbers before dialing and comply with local regulations.

## Troubleshooting
- If Twilio authentication fails, confirm `TWILIO_SID` and `TWILIO_TOKEN` are correct and the environment variables are loaded.
- If the app cannot bind to the port, ensure nothing else is using `5000` or set `FLASK_RUN_PORT`/adjust `app.run()` as needed.

## Next improvements (suggestions)
- Add a `README.md` for the top-level repo (already exists) and link to this file.
- Add `.gitignore` entry to prevent `.env` from being committed.
- Add unit tests or a small integration test harness that uses Twilio test credentials.

If you want, I can also add a `.gitignore` entry and commit it, or push the README to the remote. Tell me which you'd like next.
