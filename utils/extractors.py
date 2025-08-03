import re
from bs4 import BeautifulSoup

def extract_emails(html):
    return list(set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", html)))

def extract_phones(html):
    return list(set(re.findall(r"\+?\d[\d\s().-]{7,}", html)))

def extract_company_name(soup):
    title = soup.title.string if soup.title else "Unknown"
    return title.strip()

def extract_all_fields(url, html):
    soup = BeautifulSoup(html, "lxml")
    return {
        "company_name": extract_company_name(soup),
        "website": url,
        "emails": extract_emails(html),
        "phones": extract_phones(html),
    }
