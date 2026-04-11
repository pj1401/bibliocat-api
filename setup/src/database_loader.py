"""
DatabaseLoader class.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class DatabaseLoader:
    def __init__(self, uri: str):
        self.engine = create_engine(uri, pool_pre_ping=True)
        self.session_factory = sessionmaker(bind=self.engine)

    def load_table(self, seed_data: list, model):
        """Load seed data into a table."""
        session = self.session_factory()
        try:
            session.query(model).delete()
            session.add_all(seed_data)
            session.commit()
            print(
                f"Successfully loaded {len(seed_data)} records into {model.__name__}."
            )
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
