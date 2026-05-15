"""
BaseQueryParams schema.
module: src/util/schemas/query_params.py
"""

from pydantic import BaseModel, Field


class BaseQueryParams(BaseModel):
    limit: int = Field(20, ge=1, le=25)
    offset: int = Field(0, ge=0)
