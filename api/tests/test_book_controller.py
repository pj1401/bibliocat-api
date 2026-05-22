import pytest
from pydantic import ValidationError
from unittest.mock import create_autospec
from src.util.schemas.books.book_query_params import BookQueryParams
from src.controllers.book_controller import BookController
from src.services.book_service import BookService


@pytest.fixture
def mock_service() -> BookService:
    return create_autospec(BookService)


@pytest.fixture
def controller(mock_service: BookService):
    return BookController(book_service=mock_service)


class TestGetParams:
    def test_returns_book_query_params(self, controller: BookController):
        params = controller._get_params({"category": "fiction"})  # pyright: ignore[reportPrivateUsage]
        assert params.category == "fiction"
        assert isinstance(params, BookQueryParams)

    def test_raises_validation_error(self, controller: BookController):
        with pytest.raises(ValidationError):
            controller._get_params({"limit": "999"})  # pyright: ignore[reportPrivateUsage]
