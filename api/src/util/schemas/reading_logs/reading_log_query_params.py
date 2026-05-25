"""
ReadingLogQueryParams schema.
module: src/util/schemas/reading_logs/reading_log_query_params.py
"""

from enum import StrEnum
from src.util.schemas import BaseQueryParams


class ReadingLogSort(StrEnum):
    """Specifies the column to sort by"""

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    STARTED_AT = "started_at"
    ENDED_AT = "ended_at"


class ReadingLogQueryParams(BaseQueryParams):
    book_id: int | None = None
    book_title: str | None = None
    sort: ReadingLogSort | None = None
