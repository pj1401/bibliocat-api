"""
The ReadingLogRepository class.
module: src/repositories/reading_log_repo.py
"""

from typing import Any, Dict
from sqlalchemy import Select, func, select
from sqlalchemy.orm import selectinload
from src.repositories.writable_repo import WritableRepository
from src.util.schemas.reading_logs import ReadingLogParams
from src.util.filters.reading_log_filters import ReadingLogFilters
from src.util.models import Book, ReadingLog
from src.db.connection_manager import DatabaseConnectionManager


class ReadingLogRepository(
    WritableRepository[ReadingLog, ReadingLogFilters, ReadingLogParams]
):
    """
    Data-access layer for the reading log collection.
    """

    def __init__(
        self,
        db_manager: DatabaseConnectionManager,
        reading_log_model: type[ReadingLog],
        base_url: str,
    ):
        super().__init__(db_manager, reading_log_model, base_url)

    def get_new_model(self, arguments: ReadingLogParams) -> ReadingLog:
        return ReadingLog(
            started_at=arguments.started_at,
            ended_at=arguments.ended_at,
            user_id=arguments.user_id,
            book_id=arguments.book_id,
        )

    def _get_stmt(self, filters: ReadingLogFilters):
        stmt = select(ReadingLog).options(
            selectinload(ReadingLog.user),
            selectinload(ReadingLog.book),
        )
        return self._get_filtered_stmt(stmt, filters)

    def _get_filtered_stmt(
        self, stmt: Select[Any], filters: ReadingLogFilters
    ) -> Select[Any]:
        if filters.book_id:
            stmt = self._get_book_id_filtered_stmt(stmt, filters.book_id)
        if filters.book_title:
            stmt = self._get_book_title_filtered_stmt(stmt, filters.book_title)
        if filters.sort:
            stmt = self._get_sorted_stmt(stmt, filters.sort)
        return stmt

    def _get_book_id_filtered_stmt(
        self, stmt: Select[Any], book_id: int
    ) -> Select[Any]:
        return stmt.where(ReadingLog.book_id == book_id)

    def _get_book_title_filtered_stmt(
        self, stmt: Select[Any], book_title: str
    ) -> Select[Any]:
        return stmt.where(
            ReadingLog.book.has(func.lower(Book.title).contains(book_title.lower()))
        )

    def _get_sorted_stmt(self, stmt: Select[Any], sort_column: str) -> Select[Any]:
        return stmt.order_by(sort_column)

    def model_to_dict(self, model: ReadingLog) -> Dict[str, Any]:
        data = model.to_dict()
        data["href"] = f"{self.base_url}/api/v1/reading-logs/{model.id}"
        data["user"] = {
            "id": model.user_id,
            "href": f"{self.base_url}/api/v1/users/{model.user_id}",
        }
        data["book"] = {
            "id": model.book_id,
            "href": f"{self.base_url}/api/v1/books/{model.book_id}",
        }
        data.pop("user_id")
        data.pop("book_id")
        return data
