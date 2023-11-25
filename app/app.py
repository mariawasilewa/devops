"""
This module defines a simple Flask application.
"""
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Return a simple greeting.
    """
    return "Hello, World!"


if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000), host="0.0.0.0")
