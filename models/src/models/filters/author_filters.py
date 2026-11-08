"""
The AuthorFilters dataclass.
module: src/util/filters/author_filters.py
"""

from dataclasses import dataclass
from .base_filters import BaseFilters


@dataclass
class AuthorFilters(BaseFilters):
    name: str | None = None
    book_id: int | None = None
