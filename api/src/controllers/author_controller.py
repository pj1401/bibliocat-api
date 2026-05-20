"""
The AuthorController class.
module: src/controllers/author_controller.py
"""

from src.controllers.base_controller import BaseController
from src.services.author_service import AuthorService


class AuthorController(BaseController[AuthorService]):
    """
    AuthorController for handling the authors endpoint.
    """

    def __init__(self, author_service: AuthorService):
        super().__init__(author_service)
