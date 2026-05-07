"""
API version 1 router. Registers API endpoints.
module: src/blueprints/api/v1/router.py
"""

from flask import Blueprint, jsonify
from src.blueprints.api.v1.books.routes import books_bp
from src.blueprints.api.v1.users.routes import users_bp

router_v1_bp = Blueprint("/", __name__)
router_v1_bp.register_blueprint(books_bp, url_prefix="/books")
router_v1_bp.register_blueprint(users_bp, url_prefix="/users")


@router_v1_bp.route("/", methods=["GET"])
def get():
    response = {"message": "Welcome to version 1 of BiblioCat API!"}
    return jsonify(response)
