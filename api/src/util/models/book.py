"""
The Book model.
module: src/util/models/book.py
"""

from datetime import datetime, timezone
from sqlalchemy import (
    DateTime,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    Numeric,
)
from sqlalchemy.orm import relationship

from src.util.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = "books"
    title = Column(String, nullable=False)
    isbn = Column(String(20), unique=True)
    published_date = Column(Date)
    description = Column(String, default="")
    language = Column(String)
    page_count = Column(Integer, default=1)
    rating = Column(Numeric(precision=2, scale=1), default=0)
    voters = Column(Integer, default=0)  # Number of reviewers
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    categories = relationship("Category", secondary="categories_books", backref="books")
