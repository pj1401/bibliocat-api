"""
DatabaseLoader class.
module: src/database_loader.py
"""

from typing import Dict, List, Optional, Type, TypeVar
import numpy as np
import pandas as pd
from sqlalchemy import Table, create_engine, inspect
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
        self.seed_authors_books(books_df)
        self.seed_categories_books(books_df)

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

    def seed_authors_books(self, books_data: pd.DataFrame) -> None:
        """Seed the authors_books relationship table."""
        relationships: List[Dict[str, int]] = []
        for _, row in books_data.iterrows():
            book = self.get_book_by_isbn(row["isbn"])
            if not book:
                continue
            for author_id in row["author_ids"]:
                relationships.append({"author_id": author_id, "book_id": int(book.id)})
        if relationships:
            self.seed_relationship_table(
                relationships, authors_books_table, "author-book"
            )

    def seed_categories_books(self, books_data: pd.DataFrame) -> None:
        """Seed the categories_books relationship table."""
        relationships: List[Dict[str, int]] = []
        for _, row in books_data.iterrows():
            book = self.get_book_by_isbn(row["isbn"])
            if not book:
                continue
            category_ids = row.get("category_ids", [])
            if isinstance(category_ids, (list, np.ndarray)):
                for category_id in category_ids:
                    relationships.append(
                        {"category_id": int(category_id), "book_id": int(book.id)}
                    )
            elif pd.notna(category_ids):
                relationships.append(
                    {"category_id": int(category_ids), "book_id": int(book.id)}
                )
        if relationships:
            self.seed_relationship_table(
                relationships, categories_books_table, "category-book"
            )

    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        session = self.session_factory()
        try:
            book = session.query(Book).filter_by(isbn=isbn).first()
            if not book:
                print(f"Warning: Book with ISBN {isbn} not found in the database.")
            return book
        except SQLAlchemyError as err:
            session.rollback()
            raise err
        finally:
            session.close()

    def seed_relationship_table(
        self, relationships: List[Dict[str, int]], table: Table, relationship_name: str
    ) -> None:
        """Seed a relationship table."""
        session = self.session_factory()
        try:
            session.query(table).delete()
            session.execute(table.insert(), relationships)
            session.commit()
            print(
                f"Successfully seeded {len(relationships)} {relationship_name} relationships."
            )
        except SQLAlchemyError as err:
            session.rollback()
            raise err
        finally:
            session.close()
