"""
The UserRepository class.
module: src/repositories/user_repo.py
"""

from src.util.models.user import NewUser
from src.db.connection_manager import DatabaseConnectionManager


class UserRepository:
    def __init__(self, db_manager: DatabaseConnectionManager):
        self.db_manager = db_manager

    def create_user(self, new_user: NewUser):
        pass
