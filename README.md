# 🕸️ Company Scraper Tool

This project is a web scraping tool built in Python that extracts company-related information from a list of URLs.

## ✅ Features Implemented

- Input URLs from a file
- Data extraction (Basic level)
- Supports output in JSON and CSV
- Basic web UI using Flask
- Logging
- Basic unit tests

## 🧩 Data Extraction Level

This submission demonstrates **Basic Level** data extraction:
- Extracts title, description, email (if found), and social links from webpages

## ⚙️ Setup & Run Instructions

### 📦 1. Clone the Repository
```
git clone https://github.com/<your-username>/company-scraper.git
```
```
cd company-scraper
```

## 2. Create Virtual Environment & Install Dependencies 
```
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```


## 3. Run Command-Line Scraper
```
python main.py --urls urls.txt --output json
```

## 4. Run Web Interface
```
python app.py
```

Then open: http://127.0.0.1:5000/


