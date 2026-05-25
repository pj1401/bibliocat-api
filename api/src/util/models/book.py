"""
The Book model.
module: src/util/models/book.py
"""

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    Numeric,
)
from sqlalchemy.orm import mapped_column, relationship
from .base import BaseModel


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
    publisher_id = mapped_column(ForeignKey("publishers.id"))
    publisher = relationship("Publisher", back_populates="books")
    authors = relationship("Author", secondary="authors_books", back_populates="books")
    categories = relationship(
        "Category", secondary="categories_books", back_populates="books"
    )
    reading_logs = relationship("ReadingLog", back_populates="book")


categories_books_table = Table(
    "categories_books",
    BaseModel.metadata,
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
)
