from src.connect.Connect import CONNECT

class Snowflake(CONNECT):
    def __init__(self, name):
        from snowflake.connector import connect
        CONNECT.__init__(self, name, connect, config)
