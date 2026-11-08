"""
The Author model.
module: src/util/models/author.py
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from .base import BaseModel


class Author(BaseModel):
    __tablename__ = "authors"
    name = Column(String(255), nullable=False)
    books = relationship("Book", secondary="authors_books", back_populates="authors")


authors_books_table = Table(
    "authors_books",
    BaseModel.metadata,
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
)
