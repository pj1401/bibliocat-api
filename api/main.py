"""
The starting point of the API.
module: main.py
"""

from flask import Flask
from src.config.load_config import load_config
from src.blueprints.router import router_bp


def create_app() -> Flask:
    """Set up the application."""
    app = Flask(__name__)
    load_config(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    """Register Flask blueprints."""
    app.register_blueprint(router_bp)


if __name__ == "__main__":
    app = create_app()
    app.run()
