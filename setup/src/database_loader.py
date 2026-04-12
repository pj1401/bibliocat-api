"""
DatabaseLoader class.
module: src/database_loader.py
"""

from typing import Type
import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError


class DatabaseLoader:
    def __init__(self, uri: str, base_model: Type[DeclarativeBase]) -> None:
        self.engine = create_engine(uri, pool_pre_ping=True)
        base_model.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)

    def load_table(self, seed_data: pd.DataFrame, model: Type[DeclarativeBase]) -> None:
        """Load seed data from a DataFrame into a table."""
        session = self.session_factory()
        try:
            if inspect(self.engine).has_table(model.__tablename__):
                session.query(model).delete()

            model_instances = to_model_instance(seed_data, model)

            session.add_all(model_instances)
            session.commit()
            print(
                f"Successfully loaded {len(model_instances)} records into {model.__name__}."
            )
        except SQLAlchemyError as err:
            session.rollback()
            raise err
        finally:
            session.close()


def to_model_instance(data: pd.DataFrame, model: Type[DeclarativeBase]):
    """Convert DataFrame rows to model instances."""
    return [model(**row.to_dict()) for _, row in data.iterrows()]
