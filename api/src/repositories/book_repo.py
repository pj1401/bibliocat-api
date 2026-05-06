"""
The BookRepository class.
module: src/repositories/book_repo.py
"""

from api.src.db.connection_manager import DatabaseConnectionManager
from api.src.repositories.base_repo import BaseRepository
from api.src.util.models.book import Book


class BookRepository(BaseRepository[Book]):
    def __init__(self, db_manager: DatabaseConnectionManager):
        super().__init__(db_manager, Book)
