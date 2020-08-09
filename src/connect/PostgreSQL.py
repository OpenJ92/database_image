from src.connect.Connect import CONNECT
from psycopg2 import connect

class PostgresSQL(CONNECT):
    db_information_schema_columns = "select * from information_schema.columns"
    db_isconfig = {'column':'column_name','table':'table_name','schema':'table_schema'}
    def __init__(self, name, config):
        CONNECT.__init__(self, name, connect, config)
