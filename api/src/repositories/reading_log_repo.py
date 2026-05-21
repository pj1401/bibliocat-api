"""
The ReadingLogRepository class.
module: src/repositories/reading_log_repo.py
"""

from src.repositories.writable_repo import WritableRepository
from src.util.schemas.reading_logs import ReadingLogParams
from src.util.filters.reading_log_filters import ReadingLogFilters
from src.util.models import ReadingLog
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
