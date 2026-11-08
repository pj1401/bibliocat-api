"""
The ReadingLog model.
module: src/util/models/reading_log.py
"""

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from .base import BaseModel


class ReadingLog(BaseModel):
    __tablename__ = "reading_logs"
    started_at = Column(DateTime)
    ended_at = Column(DateTime, nullable=True)
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="reading_logs")
    book_id = mapped_column(ForeignKey("books.id"))
    book = relationship("Book", back_populates="reading_logs")
