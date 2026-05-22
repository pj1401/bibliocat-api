import pytest
from unittest.mock import create_autospec
from src.controllers.reading_log_controller import ReadingLogController
from src.services.reading_log_service import ReadingLogService


@pytest.fixture
def mock_service() -> ReadingLogService:
    return create_autospec(ReadingLogService)


@pytest.fixture
def controller(mock_service: ReadingLogService):
    return ReadingLogController(reading_log_service=mock_service)


class TestGetValidatedArguments:
    def test_returns_reading_log_params(self, controller: ReadingLogController):
        pass

    def test_raises_validation_error(self, controller: ReadingLogController):
        pass
