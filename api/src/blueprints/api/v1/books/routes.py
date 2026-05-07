"""
Defines book routes.
module: src/blueprints/api/v1/books/routes.py
"""

from flask import Blueprint, g
from src.util.models.book import Book
from src.util.schemas.book import BookSchema
from src.controllers.book_controller import BookController
from src.repositories.book_repo import BookRepository
from src.services.book_service import BookService

books_bp = Blueprint("books", __name__)


@books_bp.before_request
def before_request():
    """Create objects once per request."""
    g.book_repo = BookRepository(g.db_manager, Book)
    g.book_service = BookService(g.book_repo, BookSchema)
    g.book_controller = BookController(g.book_service)


@books_bp.route("/<int:id>", methods=["GET"])
def get_book(id: int):
    return g.book_controller.get_by_id(id)
