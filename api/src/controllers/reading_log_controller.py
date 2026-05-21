"""
The ReadingLogController class.
module: src/controllers/book_controller.py
"""

from flask_jwt_extended import get_jwt_identity
from src.util.schemas.reading_logs.reading_log_params import ReadingLogParams
from src.controllers.writable_controller import WritableController
from src.services.reading_log_service import ReadingLogService


class ReadingLogController(WritableController[ReadingLogService]):
    """
    ReadingLogController for handling the reading-log endpoint.
    """

    def __init__(self, reading_log_service: ReadingLogService):
        super().__init__(reading_log_service)

    def get_validated_arguments(self, data: dict[str, str]) -> ReadingLogParams:
        current_user = get_jwt_identity()
        data["user_id"] = current_user
        # Ignore type error since pydantic validates and coerces the types.
        return ReadingLogParams(**data)  # type: ignore[reportArgumentType]
