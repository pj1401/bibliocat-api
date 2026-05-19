"""
BaseQueryParams schema.
module: src/util/schemas/query_params.py
"""

from pydantic import BaseModel, Field


class BaseQueryParams(BaseModel):
    """
    Common query parameters for all collections.

    :var limit: Specifies the maximum number of items to return.
    :vartype limit: int
    :var offset: Specifies the starting index of the data.
    :vartype offset: int
    """

    limit: int = Field(20, ge=1, le=25)
    offset: int = Field(0, ge=0)
