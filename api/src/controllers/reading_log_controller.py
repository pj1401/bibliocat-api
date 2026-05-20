"""
The ReadingLogController class.
module: src/controllers/book_controller.py
"""

from typing import Any
from src.util.schemas.reading_logs.reading_log_post_params import ReadingLogPostParams
from src.controllers.base_controller import BaseController
from src.services.reading_log_service import ReadingLogService


class ReadingLogController(BaseController[ReadingLogService]):
    """
    ReadingLogController for handling the reading-log endpoint.
    """

    def __init__(self, reading_log_service: ReadingLogService):
        super().__init__(reading_log_service)

    def get_post_arguments(self, data: Any) -> ReadingLogPostParams:
        return ReadingLogPostParams(**data)
