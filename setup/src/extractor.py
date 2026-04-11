"""
Extractor module for extracting data from files.
"""

from collections.abc import Iterator
from typing import List
import pandas as pd


def read_csv_data(
    file_path: str, chunk_size: int, cols: List[str]
) -> Iterator[pd.DataFrame]:
    """Read data from a csv file."""
    return pd.read_csv(
        file_path,
        chunksize=chunk_size,
        usecols=cols,
    )
