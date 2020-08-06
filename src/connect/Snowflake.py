from src.connect.Connect import CONNECT
from snowflake.connector import connect

class Snowflake(CONNECT):
    def __init__(self, name):
        CONNECT.__init__(self, name, connect, config)
