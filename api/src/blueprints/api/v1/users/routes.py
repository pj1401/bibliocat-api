"""
Defines user routes.
module: src/blueprints/api/v1/users/routes.py
"""

from flask import Blueprint, g
from src.controllers.user_controller import UserController
from src.repositories.user_repo import UserRepository
from src.services.user_service import UserService

users_bp = Blueprint("users", __name__)


@users_bp.before_request
def before_request():
    """Create objects once per request."""
    g.user_repo = UserRepository(g.db_manager)
    g.user_service = UserService(g.user_repo)
    g.user_controller = UserController(g.user_service)


@users_bp.route("/register", methods=["POST"])
def create_user():
    return g.user_controller.create_user()
