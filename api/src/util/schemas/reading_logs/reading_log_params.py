"""
ReadingLogParams for validating the request body.
module: src/util/schemas/reading_logs/reading_log_params.py
"""

from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, Field


class ReadingLogParams(BaseModel):
    user_id: int = Field(..., ge=0, description="The ID of the user")
    book_id: int = Field(..., ge=0, description="The ID of the book")
    started_at: date | datetime = Field(
        ..., description="The date and time for when the reading started"
    )
    ended_at: date | datetime | None = Field(
        ..., description="The date and time for when the reading ended"
    )
