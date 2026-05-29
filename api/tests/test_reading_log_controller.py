import pytest
from datetime import date
from pydantic import ValidationError
from unittest.mock import create_autospec
from src.controllers.reading_log_controller import ReadingLogController
from src.services.reading_log_service import ReadingLogService
from src.util.schemas.reading_logs import ReadingLogParams, ReadingLogQueryParams


@pytest.fixture
def mock_service() -> ReadingLogService:
    return create_autospec(ReadingLogService)


@pytest.fixture
def controller(mock_service: ReadingLogService):
    return ReadingLogController(reading_log_service=mock_service)


class TestGetValidatedArguments:
    def test_returns_reading_log_params(self, controller: ReadingLogController):
        data = {"book_id": "2", "started_at": "2026-01-21", "ended_at": "2026-05-21"}
        params = controller.get_validated_arguments(data, user_id="42")
        assert params.user_id == 42
        assert params.book_id == 2
        assert params.started_at == date(2026, 1, 21)
        assert params.ended_at == date(2026, 5, 21)
        assert isinstance(params, ReadingLogParams)

    def test_reading_log_ended_at_is_empty(self, controller: ReadingLogController):
        data = {"book_id": "2", "started_at": "2026-01-21"}
        params = controller.get_validated_arguments(data, user_id="8")
        assert params.ended_at is None
        assert isinstance(params, ReadingLogParams)

    def test_raises_validation_error_on_missing_field(
        self, controller: ReadingLogController
    ):
        with pytest.raises(ValidationError):
            controller.get_validated_arguments({"ended_at": "2026-04-17"}, user_id="8")

    def test_raises_validation_error_on_invalid_field(
        self, controller: ReadingLogController
    ):
        with pytest.raises(ValidationError):
            controller.get_validated_arguments(
                {
                    "book_id": "not-int",
                    "started_at": "2025-11-14",
                    "ended_at": "2026-04-17",
                },
                user_id="8",
            )


class TestGetReadingLogQueryParams:
    def test_returns_reading_log_query_params(self, controller: ReadingLogController):
        params = controller._get_params({"book_title": "meditations"})  # pyright: ignore[reportPrivateUsage]
        assert params.book_title == "meditations"
        assert isinstance(params, ReadingLogQueryParams)

    def test_raises_validation_error(self, controller: ReadingLogController):
        with pytest.raises(ValidationError):
            controller._get_params({"limit": "999"})  # pyright: ignore[reportPrivateUsage]

    def test_raises_validation_error_on_invalid_sort_value(
        self, controller: ReadingLogController
    ):
        with pytest.raises(ValidationError):
            controller._get_params({"sort": "not_sort_value"})  # pyright: ignore[reportPrivateUsage]
