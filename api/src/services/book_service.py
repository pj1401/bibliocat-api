"""
The BookService class.
module: src/services/book_service.py
"""

from src.util.schemas.book import BookSchema
from src.repositories.book_repo import BookRepository
from src.services.base_service import BaseService


class BookService(BaseService[BookRepository]):
    def __init__(self, book_repo: BookRepository):
        super().__init__(book_repo, BookSchema)
