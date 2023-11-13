"""
This module contains the main Flask application.
"""

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Route for the root endpoint.

    Returns:
        str: A greeting message.
    """
    return "Hello, World!"

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000), host="0.0.0.0")
