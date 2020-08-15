from src.connect.Connect import CONNECT
from src.database.database import database

class Snowflake(database, CONNECT):
    def __init__(self, name):
        from snowflake.connector import connect
        CONNECT.__init__(self, name, connect, config)
