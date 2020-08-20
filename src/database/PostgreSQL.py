from psycopg2 import connect
from src.connect.Connect import CONNECT
from src.database.database import database

class PostgresSQL(database, CONNECT):

    ## Do we want these as class attributes or instance attributes?
    ## with open('src/database/PostgreSQL/information_schema_tree.sql') as query:
    ##     information_schema_tree_cls = query.read()

    ## with open('src/database/PostgreSQL/information_schema_graph.sql') as query:
    ##     information_schema_graph = query.read()

    ## does this belong in a yml file?
    infoconfig = \
                   {
                           'Column':'column_name',
                           'Table':'table_name',
                           'Schema':'table_schema',
                           'Database':'table_catalog'
                   }

    # Do we want to have a means for the user to supply these restrictions?
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
