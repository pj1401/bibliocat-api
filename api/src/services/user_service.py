"""
The UserService class.
module: src/services/user_service.py
"""

import bcrypt
from src.util.models.user import User
from src.util.errors.error import InvalidCredentialsError
from src.util.schemas.user import NewUser, UserArguments, UserLogin
from src.repositories.user_repo import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.repository = user_repo

    def create_user(self, user_arguments: UserArguments):
        try:
            password_hash = bcrypt.hashpw(
                user_arguments.password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            return self.repository.create_user(
                NewUser(
                    username=user_arguments.username,
                    email=user_arguments.email,
                    password_hash=password_hash,
                )
            )
        except Exception as err:
            raise err

    def login(self, user_login: UserLogin) -> User:
        try:
            user = self.repository.get_user_by_username(user_login.username)
            if user is None:
                raise InvalidCredentialsError()
            password_matches = bcrypt.checkpw(
                user_login.password.encode("utf-8"), user.password_hash.encode("utf-8")
            )
            if not password_matches:
                raise InvalidCredentialsError()
            return user
        except Exception as err:
            raise err
