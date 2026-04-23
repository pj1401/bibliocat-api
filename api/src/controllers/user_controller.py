"""
The UserController class.
module: src/controllers/user_controller.py
"""

from flask import jsonify, request
from src.util.errors.error import log_original_error
from src.services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.service = user_service

    def create_user(self):
        try:
            data = request.get_json()
            user = self.service.create_user()
            response: dict[str, int | str] = {
                "id": user.user_id,
                "username": user.username,
                "email": user.email,
                "status": 201,
            }
            # return jsonify(response), 201
            return jsonify({"status": 501, "message": "Not Implemented"}), 501
        except Exception as err:
            log_original_error(err)
            return jsonify({"status": 501, "message": "Not Implemented"}), 501
