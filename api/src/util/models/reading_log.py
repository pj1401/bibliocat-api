"""
The ReadingLog model.
module: src/util/models/reading_log.py
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from .base import BaseModel


class ReadingLog(BaseModel):
    __tablename__ = "reading_logs"
    started_at = Column(DateTime)
    ended_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
