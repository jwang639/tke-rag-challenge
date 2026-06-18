from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask import session
from flask import render_template
from flask import redirect

import json

from indexer.retriever import search
from indexer.rag import ask_rag

app = Flask(__name__)

app.secret_key = "tke-rag-demo-secret"
app.config["JSON_AS_ASCII"] = False

USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/")
def index():

    if session.get("logged_in"):
        return redirect("/chat-ui")

    return redirect("/login-ui")


@app.route("/login-ui")
def login_ui():

    return render_template(
        "login.html"
    )


@app.route("/chat-ui")
def chat_ui():

    if not session.get("logged_in"):
        return redirect("/login-ui")

    return render_template(
        "chat.html"
    )


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get(
        "username",
        ""
    )

    password = data.get(
        "password",
        ""
    )

    if (
        username == USERNAME
        and
        password == PASSWORD
    ):

        session["logged_in"] = True

        return {
            "success": True
        }

    return jsonify({
        "success": False,
        "error": "invalid username or password"
    }), 401


@app.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return {
        "success": True
    }


@app.route("/search", methods=["POST"])
def search_api():

    if not session.get("logged_in"):

        return jsonify({
            "error": "login required"
        }), 401

    data = request.get_json()

    query = data.get(
        "query",
        ""
    ).strip()

    if not query:

        return jsonify({
            "error": "query required"
        }), 400

    results = search(query)

    return Response(
        json.dumps(
            {
                "query": query,
                "count": len(results),
                "results": results
            },
            ensure_ascii=False
        ),
        mimetype="application/json"
    )


@app.route("/chat", methods=["POST"])
def chat_api():

    if not session.get("logged_in"):

        return jsonify({
            "error": "login required"
        }), 401

    data = request.get_json()

    question = data.get(
        "question",
        ""
    ).strip()

    if not question:

        return jsonify({
            "error": "question required"
        }), 400

    result = ask_rag(question)

    return Response(
        json.dumps(
            result,
            ensure_ascii=False
        ),
        mimetype="application/json"
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
