"""
The ReadingLogController class.
module: src/controllers/book_controller.py
"""

from flask import Request
from flask_jwt_extended import get_jwt_identity
from src.util.schemas.reading_logs.reading_log_params import ReadingLogParams
from src.controllers.base_controller import BaseController
from src.services.reading_log_service import ReadingLogService


class ReadingLogController(BaseController[ReadingLogService]):
    """
    ReadingLogController for handling the reading-log endpoint.
    """

    def __init__(self, reading_log_service: ReadingLogService):
        super().__init__(reading_log_service)

    def get_validated_arguments(self, request: Request) -> ReadingLogParams:
        data = request.get_json()
        current_user = get_jwt_identity()
        data["user_id"] = current_user
        return ReadingLogParams(**data)
