"""
The UserController class.
module: src/controllers/user_controller.py
"""

from flask import jsonify, request
from src.util.schemas.user import UserArguments
from src.util.errors.error import log_original_error
from src.services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.service = user_service

    def create_user(self):
        try:
            data = request.get_json()
            user_arguments = UserArguments(**data)
            user = self.service.create_user(user_arguments)
            print(user)
            response: dict[str, int | str] = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "status": 201,
            }
            return jsonify(response), 201
            # return jsonify({"status": 501, "message": "Not Implemented"}), 501
        except Exception as err:
            log_original_error(err)
            return jsonify({"status": 501, "message": "Not Implemented"}), 501
