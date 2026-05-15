"""
The BookController class.
module: src/controllers/book_controller.py
"""

from flask import jsonify, request
from src.util.errors.error import convert_to_http_error, log_original_error
from src.util.schemas.books.book_query_params import BookQueryParams
from src.controllers.base_controller import BaseController
from src.services.book_service import BookService


class BookController(BaseController[BookService]):
    def __init__(self, book_service: BookService):
        super().__init__(book_service)

    def get(self):
        try:
            params = BookQueryParams(**request.args)
            fetched = self.service.get(params)
            return jsonify({"status": 200, "data": fetched}), 200
        except Exception as err:
            log_original_error(err)
            http_err = convert_to_http_error(err)
            return jsonify(http_err.to_dict()), http_err.status
