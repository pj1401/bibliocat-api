"""
Entry point for the seed script.
"""

import os
from dotenv import load_dotenv

from src.database_loader import DatabaseLoader
from src.models import Book

# Load environment variables
load_dotenv()

SQL_URI = str(os.getenv("SQL_URI"))
db_loader = DatabaseLoader(SQL_URI)


def main():
    seed_books(db_loader)


def seed_books(db_loader: DatabaseLoader):
    books = [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            isbn="9780743273565",
            published_date="1925-04-10",
        ),
        Book(
            title="1984",
            author="George Orwell",
            isbn="9780451524935",
            published_date="1949-06-08",
        ),
    ]
    db_loader.load_table(books, Book)


if __name__ == "__main__":
    main()
