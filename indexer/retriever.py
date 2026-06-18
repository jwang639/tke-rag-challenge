import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


print("loading model...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-small"
)

print("loading index...")

index = faiss.read_index(
    "/root/rag/data/faiss.index"
)

chunks = json.load(
    open(
        "/root/rag/data/chunks.json",
        encoding="utf8"
    )
)


def search(question, top_k=5):

    vec = model.encode(
        [question],
        normalize_embeddings=True
    )

    vec = np.array(
        vec,
        dtype="float32"
    )

    scores, ids = index.search(
        vec,
        top_k
    )

    results = []

    for rank in range(top_k):

        idx = int(ids[0][rank])

        item = chunks[idx]

        results.append(
            {
                "score": float(scores[0][rank]),
                "title": item["title"],
                "date": item["date"],
                "url": item["url"],
                "content": item["content"]
            }
        )

    return results
