"""
The BookRepository class.
module: src/repositories/book_repo.py
"""

from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository
from src.util.models.book import Book


class BookRepository(BaseRepository[Book]):
    def __init__(self, db_manager: DatabaseConnectionManager, book_model: type[Book]):
        super().__init__(db_manager, book_model)
