import json
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

print("loading model...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-small"
)

print("loading chunks...")

chunks = json.load(
    open(
        "/root/rag/data/chunks.json",
        encoding="utf8"
    )
)

texts = [
    x["content"]
    for x in chunks
]

print("chunks =", len(texts))

print("embedding...")

vectors = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True,
    normalize_embeddings=True
)

vectors = np.array(
    vectors,
    dtype="float32"
)

print("shape =", vectors.shape)

np.save(
    "/root/rag/data/embeddings.npy",
    vectors
)

dimension = vectors.shape[1]

index = faiss.IndexFlatIP(
    dimension
)

index.add(vectors)

faiss.write_index(
    index,
    "/root/rag/data/faiss.index"
)

print()
print("saved:")
print("/root/rag/data/embeddings.npy")
print("/root/rag/data/faiss.index")
