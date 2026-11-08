"""
The Category model.
module: src/util/models/category.py
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"
    name = Column(String(255), nullable=False)
    books = relationship(
        "Book", secondary="categories_books", back_populates="categories"
    )
