"""
The Base SQLAlchemy model.
module: src/util/models/base.py
"""

from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """
    An abstract base model.
    see: https://docs.sqlalchemy.org/en/21/orm/inheritance.html#abstract-concrete-classes
    """

    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
