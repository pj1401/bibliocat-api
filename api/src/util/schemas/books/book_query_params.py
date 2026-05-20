"""
BookQueryParams schema.
module: src/util/schemas/books/book_query_params.py
"""

from pydantic import Field
from src.util.schemas.query_params import BaseQueryParams


class BookQueryParams(BaseQueryParams):
    category: str | None = None
    title: str | None = None
    isbn: str | None = None
    author: str | None = None
    publisher: str | None = None
    language: str | None = None
    min_rating: float | None = Field(None, ge=0.0, le=5.0)
    max_rating: float | None = Field(None, ge=0.0, le=5.0)
