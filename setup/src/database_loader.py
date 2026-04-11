"""
DatabaseLoader class.
"""

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError


class DatabaseLoader:
    def __init__(self, uri: str, base_model: DeclarativeBase):
        self.engine = create_engine(uri, pool_pre_ping=True)
        base_model.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)

    def load_table(self, seed_data: list, model: DeclarativeBase):
        """Load seed data into a table."""
        session = self.session_factory()
        try:
            if inspect(self.engine).has_table(model.__tablename__):
                session.query(model).delete()
            session.add_all(seed_data)
            session.commit()
            print(
                f"Successfully loaded {len(seed_data)} records into {model.__name__}."
            )
        except SQLAlchemyError as err:
            session.rollback()
            raise err
        finally:
            session.close()
