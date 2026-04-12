"""
DatabaseLoader class.
module: src/database_loader.py
"""

from typing import List, Type, TypeVar
import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError

from src.models import Author, Book, Category, Publisher

# Use generic type model
M = TypeVar("M", bound=DeclarativeBase)


class DatabaseLoader:
    def __init__(self, uri: str, base_model: Type[M]) -> None:
        self.engine = create_engine(uri, pool_pre_ping=True)
        base_model.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)

    def seed_database(
        self, data: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
    ) -> None:
        authors_df, publishers_df, categories_df, books_df = data
        self.seed_authors(authors_df)
        self.seed_publishers(publishers_df)
        self.seed_categories(categories_df)
        self.seed_books(books_df)

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

    def seed_categories(self, data: pd.DataFrame) -> None:
        """Seed the categories table."""
        categories = [
            Category(name=row["name"], id=row["id"]) for _, row in data.iterrows()
        ]
        self.load_table("categories", categories, Category)

    def seed_books(self, data: pd.DataFrame) -> None:
        """Seed the books table."""
        books = [
            Book(
                title=row["title"],
                isbn=row["isbn"],
                published_date=row["published_date"],
                description=row["description"],
                language=row["language"],
                page_count=row["page_count"],
                rating=row["rating"],
                voters=row["voters"],
            )
            for _, row in data.iterrows()
        ]
        self.load_table("books", books, Book)

    def load_table(self, table_name: str, data: List[M], model: Type[M]) -> None:
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
