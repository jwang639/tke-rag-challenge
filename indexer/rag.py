from indexer.retriever import search
from indexer.llm import ask_llm


def ask_rag(question):

    docs = search(question, top_k=2)

    context = "\n\n".join(
        [
            f"标题:{d['title']}\n内容:{d['content'][:500]}"
            for d in docs
        ]
    )

    prompt = f"""
你是清华大学软件学院知识库问答助手。

规则：
1. 只能根据提供资料回答。
2. 不要输出思考过程。
3. 不要输出<think>标签。
4. 不要解释推理过程。
5. 答案控制在100字以内。
6. 回答尽量简洁。
7. 找不到答案就回答：资料中未找到答案。

资料：
{context}

问题：
{question}

最终答案：
"""

    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "sources": [
            {
                "title": d["title"],
                "url": d["url"]
            }
            for d in docs
        ]
    }
