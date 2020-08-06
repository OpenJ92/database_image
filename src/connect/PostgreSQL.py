from src.connect.Connect import CONNECT
from psycopg2 import connect

class PostgresSQL(CONNECT):

    @classmethod
    def get_column_query(cls):
        pass

    @classmethod
    def get_connectivity_query(cls):
        pass

    def __init__(self, name, config):
        CONNECT.__init__(self, name, connect, config)
