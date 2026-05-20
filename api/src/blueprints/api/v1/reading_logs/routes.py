"""
Defines reading logs routes.
module: src/blueprints/api/v1/reading_logs/routes.py
"""

from flask import Blueprint, g, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.util.errors.error import (
    InvalidCredentialsError,
    convert_to_http_error,
    log_original_error,
)
from src.util.schemas.reading_logs.reading_log import ReadingLogSchema
from src.util.models import ReadingLog
from src.controllers.reading_log_controller import ReadingLogController
from src.repositories.reading_log_repo import ReadingLogRepository
from src.services.reading_log_service import ReadingLogService

reading_logs_bp = Blueprint("reading-logs", __name__)


@reading_logs_bp.before_request
def before_request():
    """Create objects once per request."""
    g.reading_log_repo = ReadingLogRepository(g.db_manager, ReadingLog, g.base_url)
    g.reading_log_service = ReadingLogService(g.reading_log_repo, ReadingLogSchema)
    g.reading_log_controller = ReadingLogController(g.reading_log_service)


@reading_logs_bp.route("", methods=["POST"])
@jwt_required()
def create_reading_log():
    try:
        current_user = get_jwt_identity()
        if current_user.user_id is None or current_user.permission_level is None:
            raise InvalidCredentialsError()
        return g.reading_log_controller.post()
    except Exception as err:
        log_original_error(err)
        http_err = convert_to_http_error(err)
        return jsonify(http_err.to_dict()), http_err.status


@reading_logs_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_reading_logs_by_id(id: int):
    return g.reading_log_controller.get_by_id(id)


@reading_logs_bp.route("", methods=["GET"])
@jwt_required()
def get_reading_logs():
    return g.reading_log_controller.get()
