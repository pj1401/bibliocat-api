"""
Transformer module.
Prepares data for database seeding.
module: src/transformer.py
"""

import pandas as pd
from typing import List, Dict, Any, cast


def transform_authors(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into authors DataFrame."""
    authors_df = (
        df["author"]
        .str.split(", ")
        .explode()
        .str.strip()
        .to_frame(name="name")
        .drop_duplicates()
        .reset_index(drop=True)
    )
    authors_df["id"] = authors_df.index + 1
    return normalize_columns(authors_df)


def transform_publishers(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into publishers DataFrame."""
    publishers_df = df[["publisher"]].drop_duplicates().reset_index(drop=True)
    publishers_df["id"] = publishers_df.index + 1
    publishers_df = publishers_df.rename(
        columns={
            "publisher": "name",
        }
    )
    return normalize_columns(publishers_df)


def transform_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into categories DataFrame."""
    categories_df = (
        df["generes"].str.split(", ").explode().str.strip().to_frame(name="name")
    )
    categories_df = categories_df.drop_duplicates().reset_index(drop=True)
    categories_df["id"] = categories_df.index + 1
    return normalize_columns(categories_df)


def transform_books(
    df: pd.DataFrame,
    publisher_map: Dict[str, int],
    category_map: Dict[str, int],
    author_map: Dict[str, int],
) -> pd.DataFrame:
    """Transform raw data into books DataFrame."""
    books_df = df.copy()
    books_df = rename_books_columns(books_df)
    books_df = clean_isbns(books_df)
    books_df = remove_duplicate_invalid_books(books_df)

    # Fill missing values and convert invalid values.
    books_df = fill_missing(books_df, "voters", 0)
    books_df = fill_missing(books_df, "rating", 0)
    books_df = fill_missing(books_df, "page_count", 1)
    int_columns = ["voters", "page_count"]
    books_df = convert_int_columns(books_df, int_columns)
    books_df["rating"] = books_df["rating"].astype(float)

    # Map publisher name to publisher_id
    books_df["publisher_id"] = books_df["publisher"].map(publisher_map)

    # Map authors (keep as a list of author_ids)
    books_df["author_ids"] = (
        books_df["author"].str.split(", ").apply(map_author_ids, args=(author_map,))
    )

    # Map categories (keep as a list of category_ids)
    books_df["category_ids"] = (
        books_df["categories_list"]
        .str.split(", ")
        .apply(map_category_ids, args=(category_map,))
    )

    # Drop unnecessary columns
    books_df = books_df.drop(columns=["publisher", "author", "categories_list"])
    return normalize_columns(books_df)


def rename_books_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rename some of the columns in the books DataFrame."""
    return df.rename(
        columns={
            "ISBN": "isbn",
            "published_date": "published_date",
            "generes": "categories_list",
        }
    )


def clean_isbns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean ISBN values."""
    df["isbn"] = df["isbn"].astype(str).str.replace("-", "", regex=False).str[:13]
    return df


def remove_duplicate_invalid_books(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicates and invalid ISBNs."""
    df = df.dropna(subset=["isbn"])
    df = df.drop_duplicates(subset=["isbn"], keep="first")
    return df


def convert_int_columns(df: pd.DataFrame, int_columns: list[str]) -> pd.DataFrame:
    """Convert specified columns to numeric, handling commas, periods, and non-numeric values."""
    for col in int_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(int)
    return df


def map_author_ids(author_list: List[str], author_map: Dict[str, int]) -> List[Any]:
    """Map author names to author IDs."""
    return [
        author_map.get(a.strip(), None) for a in author_list if a.strip() in author_map
    ]


def map_category_ids(
    category_list: List[str], category_map: Dict[str, int]
) -> List[Any]:
    """Map category names to category IDs."""
    return [
        category_map.get(c.strip(), None)
        for c in category_list
        if c.strip() in category_map
    ]


def fill_missing(
    df: pd.DataFrame, col: str, default: int | str = "Unknown"
) -> pd.DataFrame:
    """Replace NaN / None values with *default*."""
    df = df.copy()
    df[col] = df[col].fillna(default)
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase column names and strip surrounding whitespace."""
    df = df.copy()
    df.columns = [col.strip().lower() for col in df.columns]
    return df


def transform_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    authors_df = transform_authors(df)
    publishers_df = transform_publishers(df)
    categories_df = transform_categories(df)

    # Create mapping dictionaries
    author_map = cast(Dict[str, int], authors_df.set_index("name")["id"].to_dict())
    publisher_map = cast(
        Dict[str, int], publishers_df.set_index("name")["id"].to_dict()
    )
    category_map = cast(Dict[str, int], categories_df.set_index("name")["id"].to_dict())

    books_df = transform_books(df, publisher_map, category_map, author_map)
    return authors_df, publishers_df, categories_df, books_df
