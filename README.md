# TKE-RAG-Challenge

基于 Flask + FAISS + SentenceTransformer + Ollama 的本地知识库问答系统。

## 项目简介

本项目实现了一个完整的 RAG（Retrieval-Augmented Generation）知识库问答系统。

系统以清华大学软件学院新闻数据为知识来源，通过爬虫采集数据、构建向量索引、检索相关文档，并结合本地大语言模型生成答案。

主要功能：

- 知识库问答
- 来源追溯
- 本地模型推理
- 登录认证
- Web界面访问

---

## 技术架构

```text
Browser
    │
    ▼
Nginx (HTTPS)
    │
    ▼
Gunicorn
    │
    ▼
Flask
    │
    ├── FAISS
    ├── SentenceTransformer
    └── Ollama(Qwen2.5:1.5B)
```

---

## 技术栈

### 后端

- Python 3.10
- Flask
- Gunicorn

### 向量检索

- SentenceTransformer
- FAISS

### 大模型

- Ollama
- Qwen2.5:1.5B

### 部署

- Ubuntu 22.04
- Nginx
- Systemd

---

## 功能列表

### 用户功能

- 登录认证
- 知识库问答
- 来源展示
- 响应时间统计

### RAG能力

- 文档切分
- 文本向量化
- Top-K召回
- Prompt构建
- LLM生成答案

---

## 项目结构

```text
rag/
├── app.py
├── crawler/
│   ├── discover_news.py
│   └── crawl_news.py
├── data/
│   ├── news_articles.json
│   ├── chunks.json
│   ├── embeddings.npy
│   └── faiss.index
├── indexer/
│   ├── build_chunks.py
│   ├── build_index.py
│   ├── retriever.py
│   ├── rag.py
│   └── llm.py
├── templates/
│   ├── login.html
│   └── chat.html
└── requirements.txt
```

---

## 启动方式

安装依赖：

```bash
pip install -r requirements.txt
```

启动 Ollama：

```bash
ollama serve
```

拉取模型：

```bash
ollama pull qwen2.5:1.5b
```

启动服务：

```bash
gunicorn --workers 1 --bind 0.0.0.0:5000 app:app
```

---

## 检索流程

1. 用户输入问题
2. SentenceTransformer生成向量
3. FAISS检索Top-K文档
4. 构造Prompt
5. Ollama生成答案
6. 返回答案及来源

---

## 性能优化

项目开发过程中完成以下优化：

- Qwen3:4B → Qwen2.5:1.5B
- 检索上下文长度优化
- Gunicorn超时优化
- HTTPS部署
- 前端响应时间展示

优化后平均响应时间：

- 1~5秒

---

## 项目难点

### 1. HTTPS访问异常

问题：

- 页面访问后被重定向回原系统

解决：

- 排查Nginx配置
- 修正反向代理转发规则

### 2. 大模型响应时间过长

问题：

- Qwen3:4B CPU推理超过5分钟

解决：

- 更换Qwen2.5:1.5B
- 缩减Prompt长度
- 控制输出Token

优化后响应时间下降至秒级。

### 3. Gunicorn Worker Timeout

问题：

- Worker被超时杀死

解决：

- 调整timeout参数
- 优化模型推理耗时

### 4. 前后端联调问题

问题：

- 后端已返回答案
- 页面无法正确渲染

解决：

- 使用Chrome DevTools定位
- 修复前端JS渲染逻辑

---

## Git分支策略

- dev：开发环境
- uat：测试环境
- prd：生产环境

Tag：

- v1.0.0
- v1.1.0
