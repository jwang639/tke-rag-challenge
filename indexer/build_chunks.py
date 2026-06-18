import json

CHUNK_SIZE = 500
OVERLAP = 100

with open(
    "/root/rag/data/news_articles.json",
    encoding="utf8"
) as f:
    articles = json.load(f)

chunks = []

chunk_id = 0

for article in articles:

    text = article["content"].strip()

    if not text:
        continue

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunk_text = text[start:end]

        chunks.append({
            "id": chunk_id,
            "title": article["title"],
            "date": article["date"],
            "url": article["url"],
            "content": chunk_text
        })

        chunk_id += 1

        start += CHUNK_SIZE - OVERLAP

with open(
    "/root/rag/data/chunks.json",
    "w",
    encoding="utf8"
) as f:
    json.dump(
        chunks,
        f,
        ensure_ascii=False,
        indent=2
    )

print("articles =", len(articles))
print("chunks =", len(chunks))
