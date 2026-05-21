"""
The BookController class.
module: src/controllers/book_controller.py
"""

from src.util.schemas.books.book_query_params import BookQueryParams
from src.controllers.base_controller import BaseController
from src.services.book_service import BookService


class BookController(BaseController[BookService]):
    """
    BookController for handling the book endpoint.
    """

    def __init__(self, book_service: BookService):
        super().__init__(book_service)

    def _get_params(self, args: dict[str, str]) -> BookQueryParams:
        # Ignore type error since pydantic validates and coerces the types.
        return BookQueryParams(**args)  # type: ignore[reportArgumentType]
