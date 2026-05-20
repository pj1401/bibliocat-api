"""
The AuthorService class.
module: src/services/author_service.py
"""

from typing import Type
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
