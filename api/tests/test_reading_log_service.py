import pytest
from unittest.mock import create_autospec
from src.repositories import BookRepository, ReadingLogRepository, UserRepository
from src.services.reading_log_service import ReadingLogService
from src.util.errors.error import ForbiddenError
from src.util.filters.reading_log_filters import ReadingLogFilters
from src.util.schemas.reading_logs import ReadingLogSchema, ReadingLogQueryParams

@pytest.fixture
def mock_repo() -> ReadingLogRepository:
    return create_autospec(ReadingLogRepository)

@pytest.fixture
def mock_user_repo() -> UserRepository:
    return create_autospec(UserRepository)

@pytest.fixture
def mock_book_repo() -> BookRepository:
    return create_autospec(BookRepository)

@pytest.fixture
def service():
    return ReadingLogService(mock_repo, ReadingLogSchema, mock_user_repo, mock_book_repo)


class TestReadingLogAuthorize:
    def test_returns_none_on_valid_user(self, service: ReadingLogService):
        reading_log_user_id = 1
        current_user_id = 1
        assert service.authorize(reading_log_user_id, current_user_id) is None

    def test_raises_forbidden_error_on_wrong_user(
        self, service: ReadingLogService
    ):
        with pytest.raises(ForbiddenError):
            reading_log_user_id = 1
            current_user_id = 2
            service.authorize(reading_log_user_id, current_user_id)

class TestReadingLogFilters:
    def test_returns_reading_log_filter(self, service: ReadingLogService):
        filters = service._get_filters(ReadingLogQueryParams(limit=5, offset=10, book_title="meditations"))
        assert filters.limit == 5
        assert filters.offset == 10
        assert filters.book_title.lower() == "meditations"
        assert isinstance(filters, ReadingLogFilters)
