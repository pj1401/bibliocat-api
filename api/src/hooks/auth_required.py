"""
Set up auth required decorator.
module: src/hooks/auth_required.py
"""

from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTExtendedException
from src.util.errors.error import InvalidCredentialsError


def auth_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except JWTExtendedException as err:
                raise InvalidCredentialsError() from err
            return fn(*args, **kwargs)

        return decorator

    return wrapper
