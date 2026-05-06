"""
The Category model.
module: src/util/models/category.py
"""

from sqlalchemy import Column, String
from src.util.models.base import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"
    name = Column(String(255), nullable=False)
