"""
The ReadingLogController class.
module: src/controllers/book_controller.py
"""

from src.controllers.base_controller import BaseController
from src.services.reading_log_service import ReadingLogService


class ReadingLogController(BaseController[ReadingLogService]):
    """
    ReadingLogController for handling the reading-log endpoint.
    """

    def __init__(self, reading_log_service: ReadingLogService):
        super().__init__(reading_log_service)
