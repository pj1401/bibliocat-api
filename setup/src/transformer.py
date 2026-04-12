"""
Transformer module.
Prepares data for database seeding.
module: src/transformer.py
"""

import pandas as pd


def transform_authors(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into authors DataFrame."""
    authors_df = df[["author"]].drop_duplicates().reset_index(drop=True)
    authors_df["id"] = authors_df.index + 1
    authors_df = authors_df.rename(
        columns={
            "author": "name",
        }
    )
    return authors_df


def transform_publishers(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into publishers DataFrame."""
    publishers_df = df[["publisher"]].drop_duplicates().reset_index(drop=True)
    publishers_df["id"] = publishers_df.index + 1
    publishers_df = publishers_df.rename(
        columns={
            "publisher": "name",
        }
    )
    return publishers_df


def transform_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw data into categories DataFrame."""
    categories_df = (
        df["generes"].str.split(", ").explode().str.strip().to_frame(name="name")
    )
    categories_df = categories_df.drop_duplicates().reset_index(drop=True)
    categories_df["id"] = categories_df.index + 1
    return categories_df


def transform_books(
    df: pd.DataFrame, publisher_map: dict, category_map: dict
) -> pd.DataFrame:
    """Transform raw data into books DataFrame."""
    books_df = df.copy()
    books_df = books_df.rename(
        columns={
            "ISBN": "isbn",
            "published_date": "published_date",
            "generes": "categories_list",
            "description": "description",
        }
    )

    # Map publisher name to publisher_id
    books_df["publisher_id"] = books_df["publisher"].map(publisher_map)

    # Map categories (split and explode)
    books_df["categories_list"] = books_df["categories_list"].str.split(", ")
    books_df = books_df.explode("categories_list")
    books_df["category_id"] = books_df["categories_list"].map(category_map)

    # Drop unnecessary columns
    books_df = books_df.drop(columns=["publisher", "categories_list"])
    print(books_df.head())
    return books_df


def transform_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split and transform the raw DataFrame into authors, publishers, categories, and books.
    :param df: The DataFrame to transform.
    :returns: A tuple consisting of the transformed data split into four DataFrames.
    """
    authors_df = transform_authors(df)
    publishers_df = transform_publishers(df)
    categories_df = transform_categories(df)

    # Create mapping dictionaries for publishers and categories
    publisher_map = publishers_df.set_index("name")["id"].to_dict()
    category_map = categories_df.set_index("name")["id"].to_dict()

    books_df = transform_books(df, publisher_map, category_map)
    return authors_df, publishers_df, categories_df, books_df
