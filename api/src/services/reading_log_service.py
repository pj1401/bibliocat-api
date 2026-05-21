"""
The ReadingLogService class.
module: src/services/book_service.py
"""

from typing import Type
from src.repositories import BookRepository, ReadingLogRepository, UserRepository
from src.util.schemas.reading_logs import (
    ReadingLogSchema,
    ReadingLogParams,
    ReadingLogQueryParams,
)
from src.services.writable_service import WritableService


class ReadingLogService(
    WritableService[ReadingLogRepository, ReadingLogQueryParams, ReadingLogParams]
):
    """
    ReadingLogService encapsulates business logic for the book collection.
    """

    def __init__(
        self,
        reading_log_repo: ReadingLogRepository,
        reading_log_schema: Type[ReadingLogSchema],
        user_repo: UserRepository,
        book_repo: BookRepository,
    ):
        super().__init__(reading_log_repo, reading_log_schema)
        self.user_repo = user_repo
        self.book_repo = book_repo

    def validate_related(self, arguments: ReadingLogParams):
        self.user_repo.get_by_id(arguments.user_id)
        self.book_repo.get_by_id(arguments.book_id)
