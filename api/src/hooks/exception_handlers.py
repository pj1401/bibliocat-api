"""
Handle exceptions.
module: src/hooks/exception_handlers.py
"""

from flask import Flask, json
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import response


def setup_exception_handlers(app: Flask):
    @app.errorhandler(HTTPException)
    def handle_exception(err: HTTPException) -> response.Response:  # type: ignore[unused-ignore]
        """Turn default error response to JSON"""
        response = err.get_response()
        response.data = json.dumps(
            {
                "status": err.code,
                "message": err.description
                if err.code != 404
                else "The requested resource was not found.",
            }
        )
        response.content_type = "application/json"
        return response
