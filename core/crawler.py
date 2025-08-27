import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def clean_text(text: str) -> str:
    return " ".join(text.split())

def crawl(urls: list[str], fresh_days: int = 365) -> list[dict]:
    docs = []
    cutoff = datetime.now() - timedelta(days=fresh_days)

    for url in urls:
        try:
            r = requests.get(url, timeout=10, headers={"User-Agent":"Mozilla"})
            soup = BeautifulSoup(r.text, "html.parser")
            text = clean_text(soup.get_text(" "))
            if len(text) < 500: continue

            docs.append({"url": url, "text": text})
        except Exception as e:
            print(f"[!] Failed {url}: {e}")
    return docs

