"""
AuthorQueryParams schema.
module: src/util/schemas/authors/author_query_params.py
"""

from src.util.schemas.query_params import BaseQueryParams


class AuthorQueryParams(BaseQueryParams):
    name: str | None = None
    book_id: int | None = None
