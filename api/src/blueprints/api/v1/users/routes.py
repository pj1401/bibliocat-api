"""
Defines user routes.
module: src/blueprints/api/v1/users/routes.py
"""

from flask import Blueprint, jsonify

users_bp = Blueprint("users", __name__)


@users_bp.route("/register", methods=["POST"])
def create_user():
    return jsonify({"status": 501, "message": "Not Implemented"}), 501
