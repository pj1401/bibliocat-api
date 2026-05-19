"""
The BaseService class.
module: src/services/base_service.py
"""

from typing import Any, Dict, Generic, Type, TypeVar
from pydantic import BaseModel as PydanticBaseModel, ValidationError
from src.util.schemas.query_params import BaseQueryParams
from src.util.errors.error import NotFoundError, log_original_error
from src.repositories.base_repo import BaseRepository

TRepository = TypeVar("TRepository", bound=BaseRepository[Any, Any])
TSchema = TypeVar("TSchema", bound=PydanticBaseModel)
TQueryParams = TypeVar("TQueryParams", bound=BaseQueryParams)


class BaseService(Generic[TRepository, TQueryParams]):
    """
    BaseService for business logic layer.
    """

    def __init__(self, repository: TRepository, schema: Type[TSchema]):
        """
        Initialise the service with its repository dependency.

        :param repository: Repository used for data-access.
        :type repository: TRepository
        :param schema: The schema that is used for data validation.
        :type schema: Type[TSchema]
        """
        self.repository = repository
        self.schema = schema

    def get_by_id(self, id: int | str) -> Dict[str, Any]:
        """
        Fetch one record's data by matching ID.

        :param id: The id of the record.
        :type id: int | str
        :return: A dictionary representing the record data.
        :rtype: Dict[str, Any]
        """
        try:
            data = self.repository.get_by_id(id)
            self.schema.model_validate(data)
            return data
        except Exception as err:
            if isinstance(err, ValidationError):
                log_original_error(err)
                raise NotFoundError(err)
            raise err
