"""
Entry point for the seed script.
module: main.py
"""

import os
from dotenv import load_dotenv
from src.transformer import transform_data
from src.extractor import read_csv_data
from src.database_loader import DatabaseLoader
from src.models.base import BaseModel

# Load environment variables
load_dotenv()

CSV_PATH = os.getenv("CSV_PATH", "")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 5000))
SQL_URI = str(os.getenv("SQL_URI"))


def main():
    db_loader = DatabaseLoader(SQL_URI, BaseModel)
    if not db_loader.database_is_populated():
        csv_data = extract_data(CSV_PATH, CHUNK_SIZE)
        for chunk in csv_data:
            transformed_dfs = transform_data(chunk)
            db_loader.seed_database(transformed_dfs)
    else:
        print("Database already populated. Skipping seed.")
    return


def extract_data(file_path: str, chunk_size: int):
    return read_csv_data(
        file_path,
        chunk_size,
        [
            "title",
            "author",
            "rating",
            "voters",
            "description",
            "publisher",
            "page_count",
            "generes",
            "ISBN",
            "language",
            "published_date",
        ],
    )


if __name__ == "__main__":
    main()
