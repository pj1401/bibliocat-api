"""
The ReadingLogRepository class.
module: src/repositories/reading_log_repo.py
"""

from src.util.filters.reading_log_filters import ReadingLogFilters
from src.util.models import ReadingLog
from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository


class ReadingLogRepository(BaseRepository[ReadingLog, ReadingLogFilters]):
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
