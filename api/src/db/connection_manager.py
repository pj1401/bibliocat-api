"""
DatabaseConnectionManager class.
module: src/db/connection_manager.py
"""

from typing import Callable
import sqlalchemy.pool as pool
from sqlalchemy import PoolProxiedConnection
from sqlalchemy.engine.interfaces import DBAPIConnection
import psycopg2
from src.config.db_config import DbConfig


class DatabaseConnectionManager:
    def __init__(self, db_config: DbConfig):
        """
        Construct the connection pool.
        :see: https://docs.sqlalchemy.org/en/21/core/pooling.html#constructing-a-pool
        """
        self.dbname = db_config.dbname
        self.host = db_config.host
        self.user = db_config.user
        self.connection_pool = pool.QueuePool(
            self._get_connection_creator, max_overflow=10, pool_size=5
        )

    def _get_connection_creator(self) -> Callable[[], DBAPIConnection]:
        """Get a callable creator function."""

        def connection_creator() -> psycopg2.extensions.connection:
            return psycopg2.connect(user=self.user, host=self.host, dbname=self.dbname)

        return connection_creator  # pyright: ignore[reportReturnType]

    def get_connection(self) -> PoolProxiedConnection:
        """Get a connection from the pool."""
        return self.connection_pool.connect()
