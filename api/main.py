"""
The starting point of the API.
module: main.py
"""

from typing import cast
from flask import Flask
from src.config.logger_config import (
    add_logger_handler,
    get_logger_formatter,
    remove_logger_handler,
    set_logger_env,
)
from src.hooks.logging import setup_logging_hooks
from src.hooks.exception_handlers import setup_exception_handlers
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
    register_exception_handlers(app)
    configure_logger(app)

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


def register_exception_handlers(app: Flask) -> None:
    """Register exception handlers."""
    setup_exception_handlers(app)


def configure_logger(app: Flask) -> None:
    """Configure loggers."""
    set_logger_env(app)
    formatter = get_logger_formatter()
    remove_logger_handler(app)
    add_logger_handler(app, formatter)
    setup_logging_hooks(app)


if __name__ == "__main__":
    app = create_app()
    app.run()
