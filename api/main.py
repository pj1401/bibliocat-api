"""
The starting point of the API.
module: main.py
"""

from typing import cast
from flask import Flask
from src.hooks.database import setup_database_hooks
from src.config.db_config import DbConfig
from src.db.connection_manager import DatabaseConnectionManager
from src.config.load_config import load_config
from src.blueprints.router import router_bp


def create_app() -> Flask:
    """Set up the application."""
    app = Flask(__name__)
    load_config(app)
    register_db_manager(app)
    register_blueprints(app)

    return app


def register_db_manager(app: Flask) -> None:
    """Register a database manager."""
    db_manager = DatabaseConnectionManager(
        DbConfig(
            cast(str, app.config["DB_HOST"]),
            cast(str, app.config["DB_NAME"]),
            cast(str, app.config["DB_USER"]),
            cast(str, app.config["DB_PASSWORD"]),
            cast(int, app.config["DB_PORT"]),
        )
    )
    setup_database_hooks(app, db_manager)


def register_blueprints(app: Flask) -> None:
    """Register Flask blueprints."""
    app.register_blueprint(router_bp)


if __name__ == "__main__":
    app = create_app()
    app.run()
