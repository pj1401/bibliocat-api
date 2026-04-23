"""
DatabaseConnectionManager class.
module: src/db/connection_manager.py
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from src.config.db_config import DbConfig


class DatabaseConnectionManager:
    def __init__(self, db_config: DbConfig):
        """
        Initialise the engine.
        """
        self.engine = create_engine(db_config.uri, pool_pre_ping=True)
        self.session_factory = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        return self.session_factory()
