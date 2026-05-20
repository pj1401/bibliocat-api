"""
The BookService class.
module: src/services/book_service.py
"""

from typing import Type
from src.util.filters.book_filters import BookFilters
from src.util.schemas.books import BookSchema, BookQueryParams
from src.repositories.book_repo import BookRepository
from src.services.base_service import BaseService


class BookService(BaseService[BookRepository, BookQueryParams]):
    """
    BookService encapsulates business logic for the book collection.
    """

    def __init__(self, book_repo: BookRepository, book_schema: Type[BookSchema]):
        super().__init__(book_repo, book_schema)

    def _get_filters(self, params: BookQueryParams) -> BookFilters:
        return BookFilters(
            limit=params.limit,
            offset=params.offset,
            category=params.category,
            title=params.title,
            isbn=params.isbn,
            author=params.author,
            publisher=params.publisher,
            language=params.language,
            min_rating=params.min_rating,
            max_rating=params.max_rating,
            author_id=params.author_id,
        )
