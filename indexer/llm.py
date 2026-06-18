import requests


def ask_llm(prompt):

    resp = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "qwen3:4b",
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    return resp.json()["response"]
