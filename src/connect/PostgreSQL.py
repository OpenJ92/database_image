from src.connect.Connect import CONNECT
from psycopg2 import connect

class PostgresSQL(CONNECT):
    db_information_schema_columns = "select * from information_schema.columns"
    db_isconfig = {'Column':'column_name','Table':'table_name','Schema':'table_schema','Database':'table_catalog'}
    restrict = {'Column':[],'Table':[],'Schema':['information_schema', 'pg_catalog'],'Database':[]}
    def __init__(self, name, config):
        CONNECT.__init__(self, name, connect, config)
