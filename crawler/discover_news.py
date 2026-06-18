import json
import requests
import re
from urllib.parse import urljoin

BASE = "https://www.thss.tsinghua.edu.cn"

urls = set()

# 首页
pages = [
    "https://www.thss.tsinghua.edu.cn/xydt/xwdt.htm"
]

# 分页
for i in range(1, 66):
    pages.append(
        f"https://www.thss.tsinghua.edu.cn/xydt/xwdt/{i}.htm"
    )

for page in pages:

    print(page)

    r = requests.get(page, timeout=30)
    r.encoding = r.apparent_encoding

    matches = re.findall(
        r'info/\d+/\d+\.htm',
        r.text
    )

    for m in matches:
        urls.add(
            urljoin(BASE, m)
        )

print()
print("TOTAL ARTICLES =", len(urls))

with open(
    "../data/news_urls.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        sorted(list(urls)),
        f,
        ensure_ascii=False,
        indent=2
    )

print("saved to ../data/news_urls.json")
