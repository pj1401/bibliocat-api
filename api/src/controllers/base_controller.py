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
    def __init__(self, service: TService):
        self.service = service

    def get(self):
        pass

    def get_by_id(self, id: int | str):
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
