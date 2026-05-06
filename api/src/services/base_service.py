"""
The BaseService class.
module: src/services/base_service.py
"""

from typing import Any, Generic, TypeVar
from src.util.errors.error import NotFoundError
from src.repositories.base_repo import BaseRepository

TRepository = TypeVar("TRepository", bound=BaseRepository[Any])


class BaseService(Generic[TRepository]):
    def __init__(self, repository: TRepository):
        self.repository = repository

    def get(self, limit: int):
        pass

    def get_by_id(self, id: int | str):
        try:
            fetched = self.repository.get_by_id(id)
            if fetched is None:
                raise NotFoundError()
            return fetched.to_dict()
        except Exception as err:
            raise err
