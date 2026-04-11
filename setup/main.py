"""
Entry point for the seed script.
"""

import os
from dotenv import load_dotenv
from setup.src.extractor import read_csv_data
from src.database_loader import DatabaseLoader
from src.models import Base, Book

# Load environment variables
load_dotenv()

CSV_PATH = os.getenv("SQL_URI", "")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 5000))
SQL_URI = str(os.getenv("SQL_URI"))
db_loader = DatabaseLoader(SQL_URI, Base)


def main():
    csv_data = extract_data(CSV_PATH, CHUNK_SIZE)
    seed_books(db_loader)


def extract_data(file_path: str, chunk_size: int):
    return read_csv_data(
        file_path,
        chunk_size,
        [
            "title",
            "authors",
            "language",
            "ISBN",
            "rating",
            "publisher",
            "published_date",
            "voters",
            "description",
            "generes",
            "page_count",
        ],
    )


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
