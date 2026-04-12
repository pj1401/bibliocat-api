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


def transform_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split and transform the raw DataFrame into authors, publishers, categories, and books.
    :param df: The DataFrame to transform.
    :returns: A tuple consisting of the transformed data split into four DataFrames.
    """
    authors_df = transform_authors(df)
    publishers_df = transform_publishers(df)
    categories_df = transform_categories(df)
    return authors_df, publishers_df, categories_df
