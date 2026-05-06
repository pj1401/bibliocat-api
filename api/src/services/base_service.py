"""
The BaseService class.
module: src/services/base_service.py
"""

from typing import Any, Generic, Type, TypeVar
from pydantic import BaseModel as PydanticBaseModel
from src.util.errors.error import NotFoundError
from src.repositories.base_repo import BaseRepository

TRepository = TypeVar("TRepository", bound=BaseRepository[Any])
TSchema = TypeVar("TSchema", bound=PydanticBaseModel)


class BaseService(Generic[TRepository]):
    def __init__(self, repository: TRepository, schema: Type[TSchema]):
        self.repository = repository
        self.schema = schema

    def get(self, limit: int):
        pass

    def get_by_id(self, id: int | str):
        try:
            model = self.repository.get_by_id(id)
            if model is None:
                raise NotFoundError()
            data = self.repository.model_to_dict(model)
            return self.schema.model_validate(data)
        except Exception as err:
            raise err
