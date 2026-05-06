"""
The Publisher model.
module: src/util/models/publisher.py
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.util.models.base import BaseModel


class Publisher(BaseModel):
    __tablename__ = "publishers"
    name = Column(String(255), nullable=False)
    books = relationship("Book", backref="publisher")
