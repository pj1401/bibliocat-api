"""
Entry point for the seed script.
"""

import os
from dotenv import load_dotenv
from src.transformer import transform_books_data
from src.extractor import read_csv_data
from src.database_loader import DatabaseLoader
from src.models import Base, Book

# Load environment variables
load_dotenv()

CSV_PATH = os.getenv("CSV_PATH", "")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 5000))
SQL_URI = str(os.getenv("SQL_URI"))


def main():
    csv_data = extract_data(CSV_PATH, CHUNK_SIZE)
    db_loader = DatabaseLoader(SQL_URI, Base)
    for chunk in csv_data:
        print(chunk.head())
        # TODO: transform data
        transformed_df = transform_books_data(chunk)
        # seed database
        db_loader.load_table(transformed_df, Book)
        pass


def extract_data(file_path: str, chunk_size: int):
    return read_csv_data(
        file_path,
        chunk_size,
        [
            "title",
            "author",
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


if __name__ == "__main__":
    main()
