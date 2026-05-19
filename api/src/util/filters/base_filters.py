"""
The BaseFilters dataclass.
module: src/util/filters/base_filters.py
"""

from dataclasses import dataclass


@dataclass
class BaseFilters:
    limit: int = 20
    offset: int = 0
