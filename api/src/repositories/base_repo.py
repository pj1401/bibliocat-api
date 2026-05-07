"""
The BaseRepository class.
module: src/repositories/base_repo.py
"""

from typing import Any, Dict, Generic, List, TypeVar, Union
from sqlalchemy import inspect, select
from src.db.connection_manager import DatabaseConnectionManager
from sqlalchemy.orm import Session, selectinload, Mapper
from src.util.models.base import BaseModel

TModel = TypeVar("TModel", bound=BaseModel)


class BaseRepository(Generic[TModel]):
    """
    Data-access layer using a generic model.
    """

    def __init__(
        self,
        db_manager: DatabaseConnectionManager,
        model: type[TModel],
    ) -> None:
        """
        Initialise the repository with a database connection manager.

        :param db_manager: Provides scoped SQLAlchemy sessions backed by
            the application's configured database engine.
        :type db_manager: DatabaseConnectionManager
        """
        self.db_manager = db_manager
        self.model = model

    def get(self, limit: int):
        pass

    def get_by_id(self, id: int | str) -> TModel | None:
        """
        Fetch one record by matching ID.

        :param id: The id of the record.
        :type id: int | str
        :return: The matching record or None if no match is found.
        :rtype: TModel | None
        """
        session: Session | None = None
        try:
            session = self.db_manager.get_session()

            # Inspect the model class to get its relationships
            mapper: Mapper[TModel] = inspect(self.model)
            relationships = [rel.key for rel in mapper.relationships]

            stmt = select(self.model).where(self.model.id == id)
            for rel_name in relationships:
                stmt = stmt.options(selectinload(getattr(self.model, rel_name)))

            result = session.scalars(stmt).first()

            session.commit()

            # Expire and refresh attributes on the object.
            if result:
                session.refresh(result)

            return result
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()

    def model_to_dict(self, model: BaseModel) -> Dict[str, Any]:
        """Get a dictionary representing the model."""
        data = model.to_dict()
        mapper: Mapper[TModel] = inspect(self.model)
        for rel in mapper.relationships.values():
            related_objects = getattr(model, rel.key, None)
            if related_objects is None:
                continue
            data.update(self._get_relationship_dict_item(rel.key, related_objects))
        return data

    def _get_relationship_dict_item(
        self, rel_name: str, related_objects: Union[List[BaseModel], BaseModel]
    ) -> Dict[str, Any]:
        """Get a dictionary item that represents the relationship."""
        dict_item: Dict[str, Any] = {}
        if isinstance(related_objects, list):
            dict_item[f"{rel_name}_ids"] = [obj.id for obj in related_objects]
        else:
            dict_item[f"{rel_name}_id"] = related_objects.id
        return dict_item
