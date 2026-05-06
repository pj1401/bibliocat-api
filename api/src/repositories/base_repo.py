"""
The BaseRepository class.
module: src/repositories/base_repo.py
"""

from typing import Generic, TypeVar

from sqlalchemy import select
from src.db.connection_manager import DatabaseConnectionManager
from sqlalchemy.orm import Session
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
            result = session.scalars(
                select(self.model).where(self.model.id == id)
            ).first()

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
