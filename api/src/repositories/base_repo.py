"""
The BaseRepository class.
module: src/repositories/base_repo.py
"""

from typing import Generic, List, TypeVar
from api.src.db.connection_manager import DatabaseConnectionManager
from sqlalchemy.orm import Session
from src.util.models.base import Base

TModel = TypeVar("TModel", bound=Base)


class BaseRepository(Generic[TModel]):
    def __init__(
        self,
        db_manager: DatabaseConnectionManager,
        model: type[TModel],
    ) -> None:
        self.db_manager = db_manager
        self.model = model

    def get(self, limit: int) -> List[TModel]:
        pass

    def get_by_id(self, id: int | str) -> TModel | None:
        session: Session | None = None
        try:
            session = self.db_manager.get_session()
            record = session.scalars(
                select(self.model).where(self.model.id == id)
            ).first()

            session.commit()

            # Expire and refresh attributes on the object.
            if record:
                session.refresh(record)

            return record
        except Exception as err:
            if session is not None:
                session.rollback()
            raise err
        finally:
            if session is not None:
                session.close()
