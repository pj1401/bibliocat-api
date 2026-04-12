"""
DatabaseLoader class.
module: src/database_loader.py
"""

from typing import Type
import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError

from src.models import Author, Publisher


class DatabaseLoader:
    def __init__(self, uri: str, base_model: Type[DeclarativeBase]) -> None:
        self.engine = create_engine(uri, pool_pre_ping=True)
        base_model.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)

    def seed_authors(self, data: pd.DataFrame) -> None:
        """Seed the authors table."""
        authors = [Author(name=row["name"], id=row["id"]) for _, row in data.iterrows()]
        self.load_table("authors", authors, Author)

    def seed_publishers(self, data: pd.DataFrame) -> None:
        """Seed the publishers table."""
        publishers = [
            Publisher(name=row["name"], id=row["id"]) for _, row in data.iterrows()
        ]
        self.load_table("publishers", publishers, Publisher)

    def load_table(self, table_name: str, data, model: Type[DeclarativeBase]) -> None:
        """Load seed data from a DataFrame into a table."""
        session = self.session_factory()
        try:
            if inspect(self.engine).has_table(table_name):
                session.query(model).delete()
            session.add_all(data)
            session.commit()
            print(f"Successfully loaded {len(data)} {table_name}.")
        except SQLAlchemyError as err:
            session.rollback()
            raise err
        finally:
            session.close()

    def load_books_table(
        self, seed_data: pd.DataFrame, model: Type[DeclarativeBase]
    ) -> None:
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
