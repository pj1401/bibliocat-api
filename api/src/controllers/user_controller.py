"""
The UserController class.
module: src/controllers/user_controller.py
"""

from typing import cast
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from src.util.schemas.user import UserArguments, UserLogin
from src.util.errors.error import convert_to_http_error, log_original_error
from src.services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.service = user_service

    def create_user(self):
        try:
            data = request.get_json()
            user_arguments = UserArguments(**data)
            user = self.service.create_user(user_arguments)
            response: dict[str, int | str] = {
                "id": cast(int, user.id),
                "username": str(user.username),
                "email": str(user.email),
                "status": 201,
            }
            return jsonify(response), 201
        except Exception as err:
            log_original_error(err)
            http_err = convert_to_http_error(err)
            return jsonify(http_err.to_dict()), http_err.status

    def login(self):
        try:
            data = request.get_json()
            user = self.service.login(UserLogin(**data))
            access_token: str = create_access_token(
                identity={
                    "user_id": user.id,
                    "username": user.username,
                    "permission_level": user.permission_level,
                }
            )
            response: dict[str, int | str] = {
                "access_token": access_token,
                "status": 200,
            }
            return jsonify(response), 200
        except Exception as err:
            log_original_error(err)
            http_err = convert_to_http_error(err)
            return jsonify(http_err.to_dict()), http_err.status
