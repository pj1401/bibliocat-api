"""
API version 1 router. Registers API endpoints.
module: src/blueprints/api/v1/router.py
"""

from flask import Blueprint
from src.blueprints.api.v1.users.routes import users_bp

router_v1_bp = Blueprint("/", __name__)
router_v1_bp.register_blueprint(users_bp, url_prefix="/users")
