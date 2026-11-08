"""
The ReadingLogFilters dataclass.
module: src/util/filters/reading_log_filters.py
"""

from dataclasses import dataclass
from .base_filters import BaseFilters


@dataclass
class ReadingLogFilters(BaseFilters):
    book_id: int | None = None
    book_title: str | None = None
    sort: str | None = None
    user_id: int | None = None
