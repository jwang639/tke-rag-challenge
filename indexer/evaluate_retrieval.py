import json
import faiss

from sentence_transformers import SentenceTransformer

# =========================
# 配置
# =========================

TOP_K = 3

QUESTIONS = [

    "孙家广是谁",

    "王建民是谁",

    "软件学院党委书记是谁",

    "软件学院院长是谁",

    "软件学院有哪些研究所",

    "软件学院有哪些科研方向",

    "软件学院有哪些开源项目",

    "软件学院和华为有什么合作",

    "软件学院有哪些奖学金",

    "软件学院举办过哪些夏令营",

    "软件学院有哪些党建活动",

    "软件学院有哪些国际合作",

    "软件学院有哪些学术论坛",

    "软件学院有哪些校友活动",

    "软件学院有哪些人工智能相关研究",

    "软件学院有哪些工业软件研究",

    "软件学院有哪些大数据研究",

    "软件学院有哪些创新创业活动",

    "软件学院有哪些人才培养项目",

    "软件学院有哪些产学研合作"

]

# =========================
# 加载模型
# =========================

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

print(
    f"chunks={len(chunks)}"
)

# =========================
# 测试
# =========================

for q in QUESTIONS:

    print("\n")
    print("=" * 100)
    print("QUESTION:", q)
    print("=" * 100)

    vec = model.encode(
        [q],
        normalize_embeddings=True
    )

    scores, ids = index.search(
        vec,
        TOP_K
    )

    for rank in range(TOP_K):

        idx = ids[0][rank]

        item = chunks[idx]

        print()
        print(
            f"TOP {rank+1}"
        )

        print(
            f"score={scores[0][rank]:.4f}"
        )

        print(
            f"title={item['title']}"
        )

        print()

        print(
            item["content"][:300]
        )

        print()
