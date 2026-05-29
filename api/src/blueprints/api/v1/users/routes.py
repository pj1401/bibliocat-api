"""
Defines user routes.
module: src/blueprints/api/v1/users/routes.py
"""

from flask import Blueprint, g
from src.hooks.auth_required import auth_required
from src.repositories.reading_log_repo import ReadingLogRepository
from src.util.models import ReadingLog, User
from src.util.schemas.user import UserModel
from src.controllers.user_controller import UserController
from src.repositories.user_repo import UserRepository
from src.services.user_service import UserService

users_bp = Blueprint("users", __name__)


@users_bp.before_request
def before_request():
    """Create objects once per request."""
    g.reading_log_repo = ReadingLogRepository(g.db_manager, ReadingLog, g.base_url)
    g.user_repo = UserRepository(g.db_manager, User, g.base_url)
    g.user_service = UserService(g.user_repo, UserModel, g.reading_log_repo)
    g.user_controller = UserController(g.user_service)


@users_bp.route("/register", methods=["POST"])
def create_user():
    return g.user_controller.create_user()


@users_bp.route("/login", methods=["POST"])
def login_user():
    return g.user_controller.login()


@users_bp.route("/<int:id>", methods=["DELETE"])
@auth_required()
def delete(id: int):
    return g.user_controller.delete(id)
