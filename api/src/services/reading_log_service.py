"""
The ReadingLogService class.
module: src/services/book_service.py
"""

from typing import Type
from src.util.schemas.reading_logs import ReadingLogSchema, ReadingLogQueryParams
from src.repositories.reading_log_repo import ReadingLogRepository
from src.services.base_service import BaseService


class ReadingLogService(BaseService[ReadingLogRepository, ReadingLogQueryParams]):
    """
    ReadingLogService encapsulates business logic for the book collection.
    """

    def __init__(
        self,
        reading_log_repo: ReadingLogRepository,
        reading_log_schema: Type[ReadingLogSchema],
    ):
        super().__init__(reading_log_repo, reading_log_schema)
