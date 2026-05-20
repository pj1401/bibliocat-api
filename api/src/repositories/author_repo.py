"""
The AuthorRepository class.
module: src/repositories/author_repo.py
"""

from typing import Any, Dict
from sqlalchemy import Select, func, select
from sqlalchemy.orm import selectinload
from src.util.filters.author_filters import AuthorFilters
from src.util.models import Author, Book
from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository


class AuthorRepository(BaseRepository[Author, AuthorFilters]):
    """
    Data-access layer for the author collection.
    """

    def __init__(
        self,
        db_manager: DatabaseConnectionManager,
        author_model: type[Author],
        base_url: str,
    ):
        super().__init__(db_manager, author_model, base_url)

    def _get_stmt(self, filters: AuthorFilters) -> Select[Any]:
        stmt = select(Author).options(
            selectinload(Author.books),
        )
        return self._get_filtered_stmt(stmt, filters)

    def _get_filtered_stmt(
        self, stmt: Select[Any], filters: AuthorFilters
    ) -> Select[Any]:
        if filters.book_id:
            stmt = self._get_book_id_filtered_stmt(stmt, filters.book_id)
        if filters.name:
            stmt = self._get_name_filtered_stmt(stmt, filters.name)

        return stmt

    def _get_book_id_filtered_stmt(
        self, stmt: Select[Any], book_id: int
    ) -> Select[Any]:
        return stmt.where(Author.books.any(Book.id == book_id))

    def _get_name_filtered_stmt(self, stmt: Select[Any], name: str) -> Select[Any]:
        return stmt.where(func.lower(Author.name).contains(name.lower()))

    def model_to_dict(self, model: Author) -> Dict[str, Any]:
        data = model.to_dict()
        data["href"] = f"{self.base_url}/api/v1/authors/{model.id}"
        data["books"] = f"{self.base_url}/api/v1/books?author_id={model.id}"
        return data
