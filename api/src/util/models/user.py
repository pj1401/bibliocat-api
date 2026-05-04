"""
The User model.
module: src/util/models/user.py
"""

from datetime import datetime, timezone
from sqlalchemy import DateTime, Column, Integer, String
from src.util.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    permission_level = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
