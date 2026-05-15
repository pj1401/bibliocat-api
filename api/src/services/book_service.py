"""
The BookService class.
module: src/services/book_service.py
"""

from typing import Type
from src.util.filters.book_filters import BookFilters
from src.util.schemas.books.book_query_params import BookQueryParams
from src.util.schemas.books.book import BookSchema
from src.repositories.book_repo import BookRepository
from src.services.base_service import BaseService


class BookService(BaseService[BookRepository]):
    def __init__(self, book_repo: BookRepository, book_schema: Type[BookSchema]):
        super().__init__(book_repo, book_schema)

    def get(self, params: BookQueryParams):
        """Get a list of records."""
        try:
            filters = BookFilters(
                category=params.category,
                title=params.title,
                isbn=params.isbn,
                author=params.author,
                publisher=params.publisher,
                language=params.language,
                min_rating=params.min_rating,
                max_rating=params.max_rating,
            )
            fetched = self.repository.get(params.limit, params.offset, filters)
            return [self.repository.model_to_dict(row) for row in fetched]
        except Exception as err:
            raise err
