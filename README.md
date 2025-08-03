# Company Scraper

## ✅ Features Implemented

- Accepts user-provided search query or seed URLs from file
- Validates URL formatting and availability
- Extracts:
  - Company Name
  - Website URL
  - Email Addresses
  - Phone Numbers
- Stores output in JSON or CSV
- Logs errors to `logs/scraper.log`

## 🛠️ How to Run

```bash
python main.py --urls urls.txt --output json
