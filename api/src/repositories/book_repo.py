"""
The BookRepository class.
module: src/repositories/book_repo.py
"""

from typing import Any, Dict

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload
from src.util.filters.book_filters import BookFilters
from src.util.models import Author, Book, Category
from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self, db_manager: DatabaseConnectionManager, book_model: type[Book]):
        super().__init__(db_manager, book_model)

    def get(
        self, limit: int, offset: int, filters: BookFilters
    ) -> list[Dict[str, Any]]:
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            stmt = select(Book).options(
                selectinload(Book.authors),
                selectinload(Book.categories),
            )
            stmt = self._get_filtered_stmt(stmt, filters)

            result = session.scalars(stmt.offset(offset)).fetchmany(limit)
            dicts = [self.model_to_dict(row) for row in result]
            session.commit()
            return dicts
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()

    def _get_filtered_stmt(
        self, stmt: Select[Any], filters: BookFilters
    ) -> Select[Any]:
        """
        Get a statement using the filters.

        :param stmt: The base statement.
        :type stmt: Select[Any]
        :param filters: The filters.
        :type filters: BookFilters
        :return: The statement using filters.
        :rtype: Select[Any]
        """
        if filters.author:
            stmt = self._get_author_filtered_stmt(stmt, filters.author)
        if filters.category:
            stmt = self._get_category_filtered_stmt(stmt, filters.category)
        return stmt

    def _get_author_filtered_stmt(self, stmt: Select[Any], author: str):
        return stmt.where(
            Book.authors.any(func.lower(Author.name).contains(author.lower()))
        )

    def _get_category_filtered_stmt(self, stmt: Select[Any], category: str):
        return stmt.where(
            Book.categories.any(func.lower(Category.name) == func.lower(category))
        )

    def model_to_dict(self, model: Book) -> Dict[str, Any]:
        data = model.to_dict()
        data["authors_ids"] = [a.id for a in model.authors]
        data["categories_ids"] = [c.id for c in model.categories]
        data["publisher_id"] = model.publisher.id
        return data
