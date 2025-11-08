# Linkdin_Scraper

Small Selenium-based script that visits LinkedIn profile URLs listed in `profiles.txt`, scrapes the profile name and headline, and writes results to `output.csv`.

> Note: The project folder is named `Linkdin_Scraper` (spelling preserved). This README describes the script currently present in `LinkdinScraper.py`.

## What this script does
- Opens Firefox (via geckodriver) using Selenium.
- Logs into LinkedIn with the credentials embedded in the script (replace these with environment-based loading before use).
- Loads profile URLs from `profiles.txt` (one URL per line), visits each profile, and extracts the Name and Headline.
- Saves results to `output.csv`.

## Prerequisites
- Python 3.8+
- Firefox browser installed
- GeckoDriver installed and accessible (the script expects `/snap/bin/geckodriver` by default).
- Python packages: `selenium`, `pandas`.

Install dependencies (example):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install selenium pandas
```

## Configure geckodriver path
The script currently uses:

```py
service = Service("/snap/bin/geckodriver")
```

If your `geckodriver` is at a different location (for example `/usr/local/bin/geckodriver`), update that path in `LinkdinScraper.py` or make sure `geckodriver` is on your PATH.

## Credentials and safety
- The example script places LinkedIn credentials directly in the file (`send_keys("your_email_here")` / `send_keys("your_password_here")`). Do NOT commit real credentials into source control.
- A safer alternative is to load them from environment variables or a `.env` file (use `python-dotenv`) or prompt at runtime.

Example (recommended): replace hardcoded values with env var reads:

```py
import os
username = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASS")
```

and set them in your shell or `.env` file before running.

## profiles.txt format
Place one LinkedIn profile URL per line in `profiles.txt`. Example:

```
https://www.linkedin.com/in/someone-12345/
https://www.linkedin.com/in/another-person-67890/
```

## Run the script
1. Activate your virtualenv and ensure dependencies are installed.
2. Set your credentials (environment variables or updated script).
3. Ensure `profiles.txt` contains the target URLs.
4. Run:

```bash
python LinkdinScraper.py
```

By default the script runs with a visible Firefox window. To run headless (no browser UI), uncomment the `options.add_argument("--headless")` line in the script.

## Output
- On completion `output.csv` will be created/overwritten with scraped results (columns: Name, Headline, URL).

## Troubleshooting
- If Selenium raises errors about geckodriver, verify the `Service` path or install geckodriver and add it to PATH.
- If login fails, LinkedIn may be blocking automated logins or requiring CAPTCHA / 2FA — scraping LinkedIn is brittle and may fail frequently.
- If elements can't be found, LinkedIn may have changed its layout; update selectors accordingly.

## Legal & ethical notice
Automated scraping of LinkedIn may violate LinkedIn's Terms of Service and local laws. Use this script only for accounts and data you have permission to access. Consider using LinkedIn's official APIs and follow their usage policies. Be mindful of privacy and rate limits. This project is provided for educational purposes.

## Next steps / improvements
- Move credentials to environment variables or `.env` and add `.gitignore` to exclude secrets.
- Add retry/backoff logic and respectful pacing to avoid being blocked.
- Use the LinkedIn API or an approved partner API instead of scraping for production use.
- Add unit/integration tests and a headless CI job for smoke tests (careful with credentials).

If you want, I can: add a `.gitignore` entry to exclude `.env`, refactor the script to read credentials from env vars, or commit and push this README for you.
