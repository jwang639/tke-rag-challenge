from sentence_transformers import SentenceTransformer

print("loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-zh-v1.5"
)

print("model loaded")

vec = model.encode(
    "清华大学软件学院"
)

print("dimension =", len(vec))
print(vec[:10])
