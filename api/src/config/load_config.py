"""
Load env variables to a config object.
module: src/config/load_config.py
"""

import os
from dotenv import load_dotenv
from flask import Config, Flask

load_dotenv()


class TypedConfig(Config):
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    SQL_URI: str
    FLASK_DEBUG: str
    FLASK_HOST: str
    FLASK_PORT: int
    SECRET_KEY: str
    JWT_PRIVATE_KEY: str
    JWT_PUBLIC_KEY: str
    JWT_ALGORITHM: str


def load_config(app: Flask) -> None:
    """Load the config."""
    app.config.from_mapping(
        {
            "DB_HOST": os.getenv("POSTGRES_HOST"),
            "DB_NAME": os.getenv("POSTGRES_DB"),
            "DB_USER": os.getenv("POSTGRES_USER"),
            "DB_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "DB_PORT": int(os.getenv("POSTGRES_PORT", "5432")),
            "SQL_URI": os.getenv("SQL_URI"),
            "FLASK_DEBUG": os.getenv("FLASK_DEBUG", "True"),
            "FLASK_HOST": os.getenv("FLASK_HOST", "127.0.0.1"),
            "FLASK_PORT": os.getenv("FLASK_PORT", 5000),
            "SECRET_KEY": os.getenv("FLASK_SECRET_KEY"),
            "JWT_PRIVATE_KEY": os.getenv("JWT_PRIVATE_KEY"),
            "JWT_PUBLIC_KEY": os.getenv("JWT_PUBLIC_KEY"),
            "JWT_ALGORITHM": "ES512",
        }
    )
