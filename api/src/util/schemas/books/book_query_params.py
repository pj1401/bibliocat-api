"""
BookQueryParams schema.
module: src/util/schemas/books/book_query_params.py
"""

from pydantic import Field, model_validator
from src.util.schemas.query_params import BaseQueryParams


class BookQueryParams(BaseQueryParams):
    limit: int = Field(20, ge=1, le=25)
    offset: int = Field(0, ge=0)
    category: str | None = None
    title: str | None = None
    isbn: str | None = None
    author: str | None = None
    publisher: str | None = None
    language: str | None = None
    min_rating: float | None = Field(None, ge=0.0, le=5.0)
    max_rating: float | None = Field(None, ge=0.0, le=5.0)

    @model_validator(mode="before")
    @classmethod
    def strip_strings(
        cls, values: dict[str, str | int | float]
    ) -> dict[str, str | int | float]:
        """
        Remove whitespaces from field values.

        :param values: The key, value pair as a dict.
        :type values: dict[str, str | int | float]
        :return: The key, value pair. If value is a string, whitespaces are removed.
        :rtype: dict[str, str | int | float]
        """
        return {k: v.strip() if isinstance(v, str) else v for k, v in values.items()}
