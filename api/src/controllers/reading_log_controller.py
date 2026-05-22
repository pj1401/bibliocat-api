"""
The ReadingLogController class.
module: src/controllers/book_controller.py
"""

from src.util.schemas.reading_logs.reading_log_params import ReadingLogParams
from src.controllers.writable_controller import WritableController
from src.services.reading_log_service import ReadingLogService


class ReadingLogController(WritableController[ReadingLogService]):
    """
    ReadingLogController for handling the reading-log endpoint.
    """

    def __init__(self, reading_log_service: ReadingLogService):
        super().__init__(reading_log_service)

    def get_validated_arguments(
        self, data: dict[str, str], user_id: str
    ) -> ReadingLogParams:
        data["user_id"] = user_id
        # Ignore type error since pydantic validates and coerces the types.
        return ReadingLogParams(**data)  # type: ignore[reportArgumentType]
