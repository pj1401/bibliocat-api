"""
The BookFilters dataclass.
module: src/util/filters/book_filters.py
"""

from dataclasses import dataclass


@dataclass
class BookFilters:
    category: str | None = None
    title: str | None = None
    isbn: str | None = None
    author: str | None = None
    publisher: str | None = None
    language: str | None = None
    min_rating: float | None = None
    max_rating: float | None = None
