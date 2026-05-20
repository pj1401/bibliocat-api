"""
The AuthorService class.
module: src/services/author_service.py
"""

from typing import Type
from src.util.filters.author_filters import AuthorFilters
from src.util.schemas.authors import AuthorSchema, AuthorQueryParams
from src.repositories.author_repo import AuthorRepository
from src.services.base_service import BaseService


class AuthorService(BaseService[AuthorRepository, AuthorQueryParams]):
    """
    AuthorService encapsulates business logic for the author collection.
    """

    def __init__(
        self, author_repo: AuthorRepository, author_schema: Type[AuthorSchema]
    ):
        super().__init__(author_repo, author_schema)

    def _get_filters(self, params: AuthorQueryParams) -> AuthorFilters:
        return AuthorFilters(
            limit=params.limit,
            offset=params.offset,
            name=params.name,
            book_id=params.book_id,
        )
