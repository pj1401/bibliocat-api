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


def main():
    """
    The starting point for the seed script.
    """
    db_loader = DatabaseLoader(get_db_uri(), BaseModel)

    # Check if data already exists.
    if not db_loader.database_is_populated():
        csv_data = extract_data(CSV_PATH, CHUNK_SIZE)
        for chunk in csv_data:
            transformed_dfs = transform_data(chunk)
            db_loader.seed_database(transformed_dfs)
    else:
        print("Database already populated. Skipping seed.")
    return


def get_db_uri() -> str:
    """
    Get the formatted db uri.

    :return: The database URI.
    :rtype: str
    """
    POSTGRES_USER = _get_env_or_secret("POSTGRES_USER")
    POSTGRES_PASSWORD = _get_env_or_secret("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def _get_env_or_secret(
    env_var: str, default: str | int | None = None
) -> str | int | None:
    """
    Get the value of an environment variable or read it from a file if it ends with _FILE.

    :param env_var: The variable name.
    :type env_var: str
    :param default: The default value of the variable.
    :type default: str | int | None
    :return: The variable value from the file or environment variable.
    :rtype: str | int | None
    """
    file_var = f"{env_var}_FILE"
    value = None
    if file_var in os.environ:
        # Read from file
        with open(os.environ[file_var], "r") as f:
            value = f.read().strip()
    else:
        # Read from environment variable
        value = os.getenv(env_var, default)
    return value


def extract_data(file_path: str, chunk_size: int):
    """
    Docstring for extract_data

    :param file_path: The path to the csv file.
    :type file_path: str
    :param chunk_size: The number of rows to extract.
    :type chunk_size: int
    :return: An iterator with pandas DataFrames.
    :rtype: Iterator[DataFrame]
    """
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
