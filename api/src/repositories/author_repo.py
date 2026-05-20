"""
The AuthorRepository class.
module: src/repositories/author_repo.py
"""

from typing import Any, Dict
from src.util.filters.author_filters import AuthorFilters
from src.util.models import Author
from src.db.connection_manager import DatabaseConnectionManager
from src.repositories.base_repo import BaseRepository


class AuthorRepository(BaseRepository[Author, AuthorFilters]):
    """
    Data-access layer for the author collection.
    """

    def __init__(
        self,
        db_manager: DatabaseConnectionManager,
        author_model: type[Author],
        base_url: str,
    ):
        super().__init__(db_manager, author_model, base_url)

    def model_to_dict(self, model: Author) -> Dict[str, Any]:
        data = model.to_dict()
        data["href"] = f"{self.base_url}/api/v1/authors/{model.id}"
        data["books"] = f"{self.base_url}/api/v1/books?author_id={model.id}"
        return data
