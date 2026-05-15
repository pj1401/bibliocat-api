"""
The BaseRepository class.
module: src/repositories/base_repo.py
"""

from typing import Any, Dict, Generic, List, TypeVar, Union, cast
from sqlalchemy import Sequence, inspect, select
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
        :param model: The SQLAlchemy model used for data-access.
        :type model: type[TModel]
        """
        self.db_manager = db_manager
        self.model = model

    def get(self, limit: int, filters: list | None = None) -> Sequence[TModel]:
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            stmt = select(self.model)
            if filters:
                stmt = stmt.where(*filters)
            result = session.scalars(stmt).fetchmany(limit)
            session.commit()
            if result:
                for row in result:
                    session.refresh(row)
            return result
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()

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

            stmt = select(self.model).where(self.model.id == id)

            # Add relationships to the statement
            for rel in mapper.relationships.values():
                stmt = stmt.options(selectinload(getattr(self.model, rel.key)))

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
        """
        Get a dictionary representing the model.

        :param model: The model for the object.
        :type model: BaseModel
        :return: A dictionary representing the model.
        :rtype: Dict[str, Any]
        """
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
        """
        Get a dictionary item that represents the relationship.

        :param rel_name: The name of the related table.
        :type rel_name: str
        :param related_objects: A list of related objects.
        :type related_objects: Union[List[BaseModel], BaseModel]
        :return: A dictionary with a relationship that has one id or a list of ids.
        :rtype: Dict[str, Any]
        """
        dict_item: Dict[str, Any] = {}
        if isinstance(related_objects, list):
            related_list = cast(List[BaseModel], related_objects)
            dict_item[f"{rel_name}_ids"] = [obj.id for obj in related_list]
        else:
            dict_item[f"{rel_name}_id"] = related_objects.id
        return dict_item
