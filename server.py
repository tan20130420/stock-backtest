#!/usr/bin/env python3
"""三分之一投资法回测模拟器 - 静态文件服务"""
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:path>")
def static_file(path):
    return send_from_directory(".", path)


if __name__ == "__main__":
    print("=" * 50)
    print("  三分之一投资法回测模拟器")
    print("  访问: http://localhost:8080")
    print("=" * 50)
    app.run(host="0.0.0.0", port=8080, debug=False)
