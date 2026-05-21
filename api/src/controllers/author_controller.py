"""
The AuthorController class.
module: src/controllers/author_controller.py
"""

from src.controllers.base_controller import BaseController
from src.services.author_service import AuthorService
from src.util.schemas.authors import AuthorQueryParams


class AuthorController(BaseController[AuthorService]):
    """
    AuthorController for handling the authors endpoint.
    """

    def __init__(self, author_service: AuthorService):
        super().__init__(author_service)

    def _get_params(self, args: dict[str, str]) -> AuthorQueryParams:
        # Ignore type error since pydantic validates and coerces the types.
        return AuthorQueryParams(**args)  # type: ignore[reportArgumentType]
