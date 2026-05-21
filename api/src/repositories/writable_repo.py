"""
The WritableRepository class.
module: src/services/writable_repo.py
"""

from typing import Any, Dict, Generic, TypeVar
from sqlalchemy.orm import Session
from pydantic import BaseModel as PydanticBaseModel
from src.repositories.base_repo import BaseRepository
from src.util.filters.base_filters import BaseFilters
from src.util.models.base import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)
TFilters = TypeVar("TFilters", bound=BaseFilters)
TArgs = TypeVar("TArgs", bound=PydanticBaseModel)


class WritableRepository(
    BaseRepository[TModel, TFilters], Generic[TModel, TFilters, TArgs]
):
    """
    Data-access layer for the read/write collections.
    """

    def post(self, arguments: TArgs) -> Dict[str, Any]:
        """
        Create a new resource

        :param arguments: The arguments object.
        :type arguments: Type[TSchema]
        """
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            resource = self.get_new_model(arguments)
            session.add(resource)
            session.commit()
            session.refresh(resource)
            dict = self.model_to_dict(resource)
            return dict
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()

    def get_new_model(self, arguments: TArgs) -> TModel:
        """
        Map the arguments for the database model.

        :param arguments: The arguments object.
        :type arguments: Type[TSchema]
        """
        return self.model()
