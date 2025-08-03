import argparse
import os
import logging
import json
from utils.validator import validate_url
from utils.extractors import extract_all_fields
import csv 

logging.basicConfig(filename="logs/scraper.log", level=logging.INFO)

def read_urls_from_file(filepath):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_output(data, format="json"):
    os.makedirs("output", exist_ok=True)
    if format == "json":
        with open("output/result.json", "w") as f:
            json.dump(data, f, indent=4)
    elif format == "csv":
        keys = data[0].keys()
        with open("output/result.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    print(f"[✔] Output saved to output/result.{format}")

# testable wrapper for unit testing
def extract_data_from_url(url: str) -> dict:
    html = validate_url(url)
    if not html:
        return {"url": url, "error": "Invalid URL or failed to fetch content"}
    
    return extract_all_fields(url, html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", help="Path to file with seed URLs", required=True)
    parser.add_argument("--output", choices=["json", "csv"], default="json")
    args = parser.parse_args()

    # ✅ Read and clean URLs from the file
    try:
        with open(args.urls, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] The file {args.urls} was not found.")
        return

    results = []

    for url in urls:
        print(f"[INFO] Processing {url}...")
        html = validate_url(url)
        if not html:
            logging.error(f"Failed to fetch {url}")
            continue

        data = extract_all_fields(url, html)
        results.append(data)

    save_output(results, format=args.output)



if __name__ == "__main__":
    main()
