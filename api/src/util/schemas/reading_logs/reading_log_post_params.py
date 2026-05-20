"""
ReadingLogPostParams for validating the POST request body.
module: src/util/schemas/reading_logs/reading_log_post_params.py
"""

from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, Field


class ReadingLogPostParams(BaseModel):
    book_id: int
    started_at: date | datetime = Field(
        ..., description="The date and time for when the reading started"
    )
    ended_at: date | datetime | None = Field(
        ..., description="The date and time for when the reading ended"
    )
