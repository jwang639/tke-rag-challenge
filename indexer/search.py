import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "intfloat/multilingual-e5-small"
)

index = faiss.read_index(
    "/root/rag/data/faiss.index"
)

chunks = json.load(
    open(
        "/root/rag/data/chunks.json",
        encoding="utf8"
    )
)

while True:

    q = input("\n问题: ").strip()

    if not q:
        continue

    vec = model.encode(
        [q],
        normalize_embeddings=True
    )

    vec = np.array(
        vec,
        dtype="float32"
    )

    scores, ids = index.search(
        vec,
        5
    )

    print()

    for rank, idx in enumerate(ids[0]):

        item = chunks[idx]

        print("=" * 80)
        print("TOP", rank + 1)
        print("score =", scores[0][rank])
        print("title =", item["title"])
        print()
        print(item["content"][:300])
        print()
