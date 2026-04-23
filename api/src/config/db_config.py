"""
The DbConfig class.
module: src/config/db_config.py
"""


class DbConfig:
    def __init__(self, host: str, dbname: str, user: str, password: str, port: int):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
