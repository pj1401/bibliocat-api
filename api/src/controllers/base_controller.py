"""
The BaseController class.
module: src/controllers/base_controller.py
"""

from typing import Any, Dict, Generic, TypeVar
from flask import Request, jsonify, request
from pydantic import BaseModel as PydanticBaseModel
from src.services.base_service import BaseService
from src.util.schemas.query_params import BaseQueryParams
from src.util.errors.error import convert_to_http_error, log_original_error

TService = TypeVar("TService", bound=BaseService[Any, Any])
TSchema = TypeVar("TSchema", bound=PydanticBaseModel)


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

    def post(self):
        try:
            arguments = self.get_validated_arguments(request)
            resource = self.service.post(arguments)
            response = self.get_post_response(resource)
            return jsonify(response), 201
        except Exception as err:
            return self._error_response(err)

    def get_validated_arguments(self, request: Request) -> PydanticBaseModel:
        data = request.get_json()
        return PydanticBaseModel(**data)

    def get_post_response(self, resource: Dict[str, Any]) -> Dict[str, Any]:
        return resource | {
            "status": 201,
        }

    def get(self):
        """
        Get a list of records using optional query parameters.

        :return: A JSON response.
        :rtype: tuple[Response, Literal[200]] | tuple[Response, int]
        """
        try:
            params = self._get_params(request)
            fetched = self.service.get(params)
            return jsonify({"status": 200, "data": fetched}), 200
        except Exception as err:
            return self._error_response(err)

    def _get_params(self, request: Request) -> BaseQueryParams:
        """
        Get the parameters object.

        :param request: The request object that contains the query parameters.
        :type request: Request
        :return: The parameters in the form of BaseQueryParams or similar object.
        :rtype: BaseQueryParams
        """
        # Ignore type error since pydantic validates and coerces the types.
        return BaseQueryParams(**request.args)  # type: ignore

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
            return self._error_response(err)

    def _error_response(self, err: Exception):
        """
        Get the error response.

        :param err: The exception used to determine the response.
        :type err: Exception
        :return: A JSON error response.
        :rtype: tuple[Response, int]
        """
        log_original_error(err)
        http_err = convert_to_http_error(err)
        return jsonify(http_err.to_dict()), http_err.status
