"""
The ReverseProxied class.
module: src/config/reverse_proxied.py
"""

from wsgiref.types import StartResponse, WSGIEnvironment
from flask import Flask


class ReverseProxied:
    """
    Helper class for handling reverse proxy.
    """

    def __init__(self, app: Flask):
        self.app = app

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse):
        script_name = environ.get("HTTP_X_SCRIPT_NAME", "")
        if script_name:
            environ["SCRIPT_NAME"] = script_name
            path_info = environ["PATH_INFO"]
            if path_info.startswith(script_name):
                environ["PATH_INFO"] = path_info[len(script_name) :]
        return self.app(environ, start_response)
