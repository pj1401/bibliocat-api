"""
The BookController class.
module: src/controllers/book_controller.py
"""

from src.controllers.base_controller import BaseController
from src.services.book_service import BookService


class BookController(BaseController[BookService]):
    def __init__(self, book_service: BookService):
        super().__init__(book_service)
