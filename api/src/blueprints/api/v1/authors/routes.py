"""
Defines author routes.
module: src/blueprints/api/v1/authors/routes.py
"""

from flask import Blueprint, g
from src.util.models import Author
from src.controllers.author_controller import AuthorController
from src.repositories.author_repo import AuthorRepository
from src.services.author_service import AuthorService

authors_bp = Blueprint("authors", __name__)


@authors_bp.before_request
def before_request():
    """Create objects once per request."""
    g.author_repo = AuthorRepository(g.db_manager, Author)
    g.author_service = AuthorService(g.author_repo, AuthorSchema)
    g.author_controller = AuthorController(g.author_service)


@authors_bp.route("/<int:id>", methods=["GET"])
def get_author_by_id(id: int):
    return g.author_controller.get_by_id(id)


@authors_bp.route("", methods=["GET"])
def get_authors():
    return g.author_controller.get()
