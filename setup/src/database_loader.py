"""
DatabaseLoader class.
module: src/database_loader.py
"""

from typing import List, Type, TypeVar
import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError

from src.models import (
    Author,
    Book,
    Category,
    Publisher,
    authors_books_table,
    categories_books_table,
)

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
        """Seed the books table and its relationships."""
        books = [
            Book(
                title=row["title"],
                isbn=row["isbn"],
                published_date=row["published_date"],
                description=row.get("description", ""),
                language=row.get("language", ""),
                page_count=row["page_count"],
                rating=row["rating"],
                voters=row["voters"],
                publisher_id=row["publisher_id"],
            )
            for _, row in data.iterrows()
        ]
        # Seed books
        self.load_table("books", books, Book)
        self.seed_authors_books_table()
        self.seed_categories_books_table()

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

    def seed_authors_books_table(
        self,
    ) -> None:
        """Seed the authors_books table."""
        session = self.session_factory()
        authors_books = [
            {"author_id": author_id, "book_id": book.id}
            for book in session.query(Book).all()
            for author_id in book.authors
            if author_id is not None
        ]
        if authors_books:
            session.execute(authors_books_table.insert().values(authors_books))
            session.commit()

    def seed_categories_books_table(
        self,
    ) -> None:
        """Seed the categories_books table."""
        session = self.session_factory()
        categories_books = [
            {"category_id": category_id, "book_id": book.id}
            for book in session.query(Book).all()
            for category_id in book.categories
            if category_id is not None
        ]
        if categories_books:
            session.execute(categories_books_table.insert().values(categories_books))
            session.commit()

    def seed_relationship_table(self) -> None:
        """Seed a relationship table."""
        session = self.session_factory()
