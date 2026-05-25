"""
The Publisher model.
module: src/util/models/publisher.py
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel


class Publisher(BaseModel):
    __tablename__ = "publishers"
    name = Column(String(255), nullable=False)
    books = relationship("Book", back_populates="publisher")
