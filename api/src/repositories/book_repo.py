"""
The BookRepository class.
module: src/repositories/book_repo.py
"""

from sqlalchemy import Sequence, func, select
from sqlalchemy.orm import Session, selectinload
# from src.util.models.author import Author
from src.util.filters.book_filters import BookFilters
from src.util.models.category import Category
from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository
from src.util.models.book import Book


class BookRepository(BaseRepository[Book]):
    def __init__(self, db_manager: DatabaseConnectionManager, book_model: type[Book]):
        super().__init__(db_manager, book_model)
    
    def get(self, limit: int, offset: int, filters: BookFilters) -> Sequence[Book]:
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            stmt = (
                select(Book)
                .options(
                    selectinload(Book.authors),
                    selectinload(Book.categories),
                )
            )

            if filters.category:
                stmt = stmt.where(
                    Book.categories.any(
                        func.lower(Category.name) == func.lower(filters.category)
                    )
                )

            result = session.scalars(stmt.offset(offset)).fetchmany(limit)
            session.commit()
            # TODO: Fix session error.
            if result:
                for row in result:
                    session.refresh(row)
            return result
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()

    def get_by_category(self, category_name: str, limit: int) -> Sequence[Book]:
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            stmt = (
                select(Book)
                .where(
                    Book.categories.any(
                        func.lower(Category.name) == func.lower(category_name)
                    )
                )
                .options(
                    selectinload(Book.authors),
                    selectinload(Book.categories),
                )
            )
            result = session.scalars(stmt).fetchmany(limit)
            session.commit()
            if result:
                for row in result:
                    session.refresh(row)
            return result
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()
