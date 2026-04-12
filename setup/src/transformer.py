"""
Transformer module.
Prepares data for database seeding.
module: src/transformer.py
"""

import pandas as pd


def transform_books_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the raw DataFrame to match the Book model schema.
    :param df: The DataFrame to transform.
    :returns: The transformed DataFrame.
    """
    # Rename columns to match the Book model
    transformed_df = df.rename(
        columns={
            "ISBN": "isbn",
            "published_date": "published_date",
            "generes": "categories",
        }
    )

    return transformed_df
