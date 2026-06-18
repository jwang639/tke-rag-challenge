import json
import re
import time
import requests
from bs4 import BeautifulSoup

INPUT_FILE = "../data/news_urls.json"
OUTPUT_FILE = "../data/news_articles.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

with open(INPUT_FILE, encoding="utf-8") as f:
    urls = json.load(f)

articles = []

for idx, url in enumerate(urls, start=1):

    try:
        print(f"[{idx}/{len(urls)}] {url}")

        resp = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        resp.encoding = resp.apparent_encoding

        soup = BeautifulSoup(
            resp.text,
            "lxml"
        )

        title_node = soup.select_one(".up-title")

        title = (
            title_node.get_text(strip=True)
            if title_node else ""
        )

        content_node = soup.select_one(
            ".v_news_content"
        )

        content = (
            content_node.get_text(
                "\n",
                strip=True
            )
            if content_node else ""
        )

        date_match = re.search(
            r"20\d{2}-\d{2}-\d{2}",
            resp.text
        )

        publish_date = (
            date_match.group(0)
            if date_match else ""
        )

        articles.append({
            "title": title,
            "date": publish_date,
            "url": url,
            "content": content
        })

        time.sleep(0.3)

    except Exception as e:
        print("ERROR:", url)
        print(e)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        articles,
        f,
        ensure_ascii=False,
        indent=2
    )

print()
print("================================")
print("saved:", len(articles))
print("file :", OUTPUT_FILE)
print("================================")
