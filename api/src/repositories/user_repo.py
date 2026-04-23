"""
The UserRepository class.
module: src/repositories/user_repo.py
"""

from psycopg2.extras import RealDictCursor
from src.util.models.user import NewUser, UserModel
from src.db.connection_manager import DatabaseConnectionManager


class UserRepository:
    def __init__(self, db_manager: DatabaseConnectionManager):
        self.db_manager = db_manager

    def create_user(self, new_user: NewUser):
        try:
            query = """
                    INSERT INTO users (username, email, password_hash)
                    VALUES (%s, %s, %s)
                    RETURNING user_id, username, email, permission_level
                    """
            conn = self.db_manager.get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                query, (new_user.username, new_user.email, new_user.password_hash)
            )
            fetched = cursor.fetchone()
            user = UserModel(**fetched)
            conn.close()
            return user
        except Exception as err:
            raise err
