THSS RAG Chatbot

基于清华大学软件学院官网构建的检索增强生成（RAG）问答系统。

本项目为 TKE Interview Lab RAG Challenge 实现，支持全站内容检索、引用溯源、登录认证以及 Web 聊天界面。

⸻

项目功能

* 清华大学软件学院官网内容爬取
* 新闻文章解析与清洗
* 文本 Chunk 切分
* 向量化 Embedding
* FAISS 向量检索
* Ollama 本地大模型问答
* 登录认证保护
* 来源引用展示
* HTTPS 部署
* Gunicorn + Nginx 生产部署

⸻

系统架构

清华大学软件学院官网
           │
           ▼
      爬虫采集
           │
           ▼
      数据清洗
           │
           ▼
      Chunk切分
           │
           ▼
Embedding模型
(multilingual-e5-small)
           │
           ▼
      FAISS索引
           │
           ▼
      Retriever
           │
           ▼
      Ollama
      Qwen3:4B
           │
           ▼
      Web Chat

⸻

技术栈

后端

* Flask
* Gunicorn
* Requests

检索

* FAISS
* Sentence Transformers
* multilingual-e5-small

大模型

* Ollama
* Qwen3:4B

部署

* Ubuntu Linux
* Nginx
* systemd

⸻

项目目录

app.py
crawler/
├── discover_news.py
└── crawl_news.py
indexer/
├── build_chunks.py
├── build_index.py
├── retriever.py
├── rag.py
├── llm.py
data/
├── chunks.json
├── embeddings.npy
├── faiss.index
├── news_articles.json
└── news_urls.json
templates/
├── login.html
└── chat.html

⸻

环境安装

创建虚拟环境：

python -m venv venv
source venv/bin/activate

安装依赖：

pip install -r requirements.txt

⸻

启动方式

开发模式：

python app.py

生产模式：

gunicorn -w 1 -b 0.0.0.0:5000 app:app

⸻

登录账号

演示账号：

用户名：

admin

密码：

admin123

⸻

重建索引

如需重新抓取并生成索引：

发现新闻链接：

python crawler/discover_news.py

抓取新闻正文：

python crawler/crawl_news.py

生成文本切片：

python indexer/build_chunks.py

生成向量索引：

python indexer/build_index.py

⸻

部署说明

项目部署于 Ubuntu 服务器。

部署架构：

Internet
   │
   ▼
 Nginx
   │
   ▼
Gunicorn
   │
   ▼
 Flask
   │
   ▼
 RAG

系统使用 systemd 管理服务，实现开机自动启动。

⸻

认证说明

未登录用户无法访问聊天页面及问答接口。

认证流程：

/login-ui
      │
      ▼
用户名密码验证
      │
      ▼
Session认证
      │
      ▼
/chat-ui

⸻

引用机制

系统在生成回答时会返回检索到的原始文章来源。

返回内容包含：

* 文章标题
* 原始链接
* 回答内容

用于保证回答可追溯性与可信度。

⸻

预构建索引

为方便评审快速启动项目，仓库中包含以下预构建文件：

data/chunks.json
data/embeddings.npy
data/faiss.index

评审人员无需重新爬取网站即可直接运行系统。

⸻

已知限制

* 当前使用 CPU 推理，响应速度较 GPU 环境慢
* 当前使用单机 FAISS 索引
* 未实现多轮对话记忆
* 未实现流式输出

⸻

作者:Jiahao Wang
