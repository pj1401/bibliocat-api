"""
The BookController class.
module: src/controllers/book_controller.py
"""

from flask import jsonify, request
from src.util.schemas.books.book_query_params import BookQueryParams
from src.controllers.base_controller import BaseController
from src.services.book_service import BookService


class BookController(BaseController[BookService]):
    """
    BookController for handling the book endpoint.
    """

    def __init__(self, book_service: BookService):
        super().__init__(book_service)

    def get(self):
        try:
            # Ignore type error since pydantic validates and coerces the types.
            params = BookQueryParams(**request.args)  # type: ignore

            fetched = self.service.get(params)
            return jsonify({"status": 200, "data": fetched}), 200
        except Exception as err:
            return self._error_response(err)
