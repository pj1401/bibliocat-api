"""
The UserRepository class.
module: src/repositories/user_repo.py
"""

from sqlalchemy import exc
from sqlalchemy.orm import Session
from src.util.errors.error import UniqueViolationError
from src.util.models.user import User
from src.util.schemas.user import NewUser
from src.db.connection_manager import DatabaseConnectionManager


class UserRepository:
    def __init__(self, db_manager: DatabaseConnectionManager):
        self.db_manager = db_manager

    def create_user(self, new_user: NewUser):
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            user = User(
                username=new_user.username,
                email=new_user.email,
                password_hash=new_user.password_hash,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except exc.IntegrityError as err:
            if session is not None:
                session.rollback()
            raise UniqueViolationError(err)
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()
