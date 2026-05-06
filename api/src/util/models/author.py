"""
The Author model.
module: src/util/models/author.py
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.util.models.base import BaseModel


class Author(BaseModel):
    __tablename__ = "authors"
    name = Column(String(255), nullable=False)
    books = relationship("Book", secondary="authors_books", backref="authors")
