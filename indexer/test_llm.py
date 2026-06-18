import requests

resp = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "qwen3:4b",
        "prompt": "你是谁",
        "stream": False
    },
    timeout=120
)

print(resp.json()["response"])
