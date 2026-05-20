"""
NewReadingLog dataclass is used for creating new reading log resources.
module: src/util/schemas/reading_logs/new_reading_log.py
"""

from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class NewReadingLog:
    started_at: date | datetime
    ended_at: date | datetime | None
    user_id: int
    book_id: int
