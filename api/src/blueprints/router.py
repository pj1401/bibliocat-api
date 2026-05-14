"""
The main router that registers the api routes.
module: src/blueprints/router.py
"""

from typing import cast
from flask import Blueprint, jsonify, current_app
from src.blueprints.api.v1.router import router_v1_bp

router_bp = Blueprint("/", __name__)
router_bp.register_blueprint(router_v1_bp, url_prefix="/api/v1")


@router_bp.route("/", methods=["GET"])
def get():
    base_url = cast(str, current_app.config["BASE_URL"])
    response = {
        "message": "Welcome to BiblioCat API!",
        "version 1": f"{base_url}/api/v1",
    }
    return jsonify(response)
