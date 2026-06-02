"""
Defines reading logs routes.
module: src/blueprints/api/v1/reading_logs/routes.py
"""

from flask import Blueprint, g
from src.repositories import BookRepository, ReadingLogRepository, UserRepository
from src.hooks.auth_required import auth_required
from src.util.schemas.reading_logs.reading_log import ReadingLogSchema
from src.util.models import Book, ReadingLog, User
from src.controllers.reading_log_controller import ReadingLogController
from src.services.reading_log_service import ReadingLogService

reading_logs_bp = Blueprint("reading-logs", __name__)


@reading_logs_bp.before_request
def before_request():
    """Create objects once per request."""
    g.user_repo = UserRepository(g.db_manager, User, g.base_url)
    g.book_repo = BookRepository(g.db_manager, Book, g.base_url)
    g.reading_log_repo = ReadingLogRepository(g.db_manager, ReadingLog, g.base_url)
    g.reading_log_service = ReadingLogService(
        g.reading_log_repo, ReadingLogSchema, g.user_repo, g.book_repo
    )
    g.reading_log_controller = ReadingLogController(g.reading_log_service)


@reading_logs_bp.route("", methods=["POST"])
@auth_required()
def create_reading_log():
    return g.reading_log_controller.post()


@reading_logs_bp.route("/<int:id>", methods=["GET"])
@auth_required()
def get_reading_log_by_id(id: int):
    return g.reading_log_controller.get_by_id(id)


@reading_logs_bp.route("", methods=["GET"])
@auth_required()
def get_reading_logs():
    return g.reading_log_controller.get()


@reading_logs_bp.route("/<int:id>", methods=["PUT"])
@auth_required()
def update(id: int):
    return g.reading_log_controller.update(id)


@reading_logs_bp.route("/<int:id>", methods=["DELETE"])
@auth_required()
def delete_reading_log(id: int):
    return g.reading_log_controller.delete(id)
