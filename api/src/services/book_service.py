"""
The BookService class.
module: src/services/book_service.py
"""

from typing import Type

from src.util.schemas.books.book import BookSchema
from src.repositories.book_repo import BookRepository
from src.services.base_service import BaseService


class BookService(BaseService[BookRepository]):
    def __init__(self, book_repo: BookRepository, book_schema: Type[BookSchema]):
        super().__init__(book_repo, book_schema)
