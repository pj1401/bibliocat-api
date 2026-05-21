"""
The WritableController class.
module: src/controllers/writable_controller.py
"""

from typing import Any, Dict, TypeVar
from flask import Request, jsonify, request
from pydantic import BaseModel as PydanticBaseModel
from src.controllers.base_controller import BaseController
from src.services.writable_service import WritableService

TService = TypeVar("TService", bound=WritableService[Any, Any])


class WritableController(BaseController[TService]):
    """
    WritableController for handling read/write endpoints.
    """

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
