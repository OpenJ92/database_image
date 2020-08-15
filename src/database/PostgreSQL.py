from psycopg2 import connect
from src.connect.Connect import CONNECT

class PostgresSQL(CONNECT):

    db_information_schema_columns = "select * from information_schema.columns"
    db_isconfig = \
                   {
                           'Column':'column_name',
                           'Table':'table_name',
                           'Schema':'table_schema',
                           'Database':'table_catalog'
                   }

    restrict = \
                {
                        'Column':[],
                        'Table':[],
                        'Schema':['information_schema', 'pg_catalog'],
                        'Database':[]
                }

    def __init__(self, name, config):
        CONNECT.__init__(self, name, connect, config)
        self.get_information_schema_tree()
        self.get_information_schema_graph()

    def get_information_schema_tree(self):
        with open('src/database/PostgreSQL/information_schema_tree.sql') as query:
            self.information_schema_tree = query.read()

    def get_information_schema_graph(self):
        with open('src/database/PostgreSQL/information_schema_graph.sql') as query:
            self.information_schema_graph = query.read()
