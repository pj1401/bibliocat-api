"""
The starting point of the API.
module: main.py
"""

from flask import Flask

def create_app() -> Flask:
    """Set up the application."""
    app = Flask(__name__)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
