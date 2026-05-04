"""
The BaseService class.
module: src/services/base_service.py
"""

from typing import Any, Generic, TypeVar
from api.src.repositories.base_repo import BaseRepository

TRepository = TypeVar("TRepository", bound=BaseRepository[Any])


class BaseService(Generic[TRepository]):
    def __init__(self, repository: TRepository):
        self.repository = repository

    def get(self, limit: int):
        pass

    def get_by_id(self, id: int | str):
        try:
            return self.repository.get_by_id(id)
        except Exception as err:
            raise err
