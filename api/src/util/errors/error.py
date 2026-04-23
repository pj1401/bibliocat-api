"""
Custom errors and helper functions.
module: src/util/errors/error.py
"""

import logging


def log_original_error(err: Exception):
    logging.error(f"Error occurred: {type(err).__name__}, Original exception: {err}")
