"""
The BaseController class.
module: src/controllers/base_controller.py
"""

from typing import Any, Generic, TypeVar
from flask import jsonify
from src.services.base_service import BaseService
from src.util.errors.error import convert_to_http_error, log_original_error

TService = TypeVar("TService", bound=BaseService[Any])


class BaseController(Generic[TService]):
    """
    BaseController for HTTP routes.
    """

    def __init__(self, service: TService):
        """
        Initialise the controller with its service dependency.

        :param service: The service that performs business logic.
        :type service: TService
        """
        self.service = service

    def get(self):
        pass

    def get_by_id(self, id: int | str):
        """
        Fetch one record's data by matching ID.

        :param id: The id of the record.
        :type id: int | str
        :return: A response in JSON.
        :rtype: tuple[Response, Literal[200]] | tuple[Response, int]
        """
        try:
            fetched = self.service.get_by_id(id)
            response: dict[str, int | Any | None] = {
                "status": 200,
                "data": fetched,
            }
            return jsonify(response), 200
        except Exception as err:
            log_original_error(err)
            http_err = convert_to_http_error(err)
            return jsonify(http_err.to_dict()), http_err.status
