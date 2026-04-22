"""
The main router that registers the api routes.
module: src/blueprints/router.py
"""

from flask import Blueprint
from src.blueprints.api.v1.router import router_v1_bp

router_bp = Blueprint("/", __name__)
router_bp.register_blueprint(router_v1_bp, url_prefix="/api/v1")
