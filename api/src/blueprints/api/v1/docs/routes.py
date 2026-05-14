"""
Defines the docs route.
module: src/blueprints/api/v1/docs/routes.py
"""

from typing import cast
from flask import current_app
from flask_swagger_ui import get_swaggerui_blueprint

path_prefix = cast(str, current_app.config["PATH_PREFIX"])
SWAGGER_URL = f"{path_prefix}/api/v1/docs"
API_URL = "/static/BiblioCat API v1.openapi.json"
docs_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "BiblioCat API v1",
        "docExpansion": "none",
        "persistAuthorization": True,
    },
)
