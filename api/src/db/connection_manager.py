"""
DatabaseConnectionManager class.
module: src/db/connection_manager.py
"""

from sqlalchemy import PoolProxiedConnection
import sqlalchemy.pool as pool
import psycopg2
from src.config.db_config import DbConfig


class DatabaseConnectionManager:
    def __init__(self, db_config: DbConfig):
        self.dbname = db_config.dbname
        self.host = db_config.host
        self.user = db_config.user
        self.connection_pool = pool.QueuePool(
            self._get_connection_creator, max_overflow=10, pool_size=5
        )

    def _get_connection_creator(self):
        """Get the creator function."""
        conn = psycopg2.connect(user=self.user, host=self.host, dbname=self.dbname)
        return conn

    def get_connection(self) -> PoolProxiedConnection:
        """Get a connection from the pool."""
        return self.connection_pool.connect()
