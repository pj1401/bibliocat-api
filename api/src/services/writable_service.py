"""
The WritableService class.
module: src/services/writable_service.py
"""

from typing import Any, TypeVar
from pydantic import BaseModel as PydanticBaseModel
from src.util.schemas.query_params import BaseQueryParams
from src.repositories.writable_repo import WritableRepository
from src.services.base_service import BaseService

TRepository = TypeVar("TRepository", bound=WritableRepository[Any, Any, Any])
TQueryParams = TypeVar("TQueryParams", bound=BaseQueryParams)


class WritableService(BaseService[TRepository, TQueryParams]):
    def post(self, arguments: PydanticBaseModel):
        try:
            return self.repository.post(arguments)
        except Exception as err:
            raise err
