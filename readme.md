# Gmail Automation Tool

CLI tool to automate Gmail inbox management via IMAP.

Processes large numbers of emails efficiently using UID-based operations.

---

## What it does

* Fetches emails from Gmail via IMAP
* Extracts sender domains
* Shows domain statistics
* Moves emails in bulk (e.g. to spam)

---

## Why this project

Built to solve a real problem: handling thousands of emails quickly.

Key focus:

* performance (UID instead of message IDs)
* clean structure (services / utils / UI separation)
* real data handling (not a toy project)

---

## Run it

```bash
git clone https://github.com/antoniomontiljo882-max/Gmail-client.git
cd Gmail-client
pip install -r requirements.txt
```

Create `.env`:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

Run:

```bash
python main.py
```

---

## Requirements

* Gmail account
* IMAP enabled
* Google App Password (not normal password)

---

## Structure

* `services/` → IMAP logic
* `UTILS/` → helpers
* `UI/` → CLI
* `main.py` → entry point

---

## Notes

* Designed for local use
* Uses real Gmail data
* Tested with large inboxes

---

## Next steps

* rule-based automation
* logging system
* better UX
