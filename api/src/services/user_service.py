"""
The UserService class.
module: src/services/user_service.py
"""

from src.repositories.user_repo import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.repository = user_repo

    def create_user(self):
        pass
