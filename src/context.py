from src.connect.dispatcher import connect
from src.struct.tree import Tree
from src.objects.dynamicnodes import __construct_nodes__

from pandas import read_sql

class Context(object):
    def __init__(self, database, name, config):
        self._connection = connect(database, name, config).connection

        with self._connection as conn:
            self._columns =\
                    read_sql("select * from information_schema.columns",conn) ## V 

        db_config = {'column':'column_name','table':'table_name','schema':'table_schema'}
        _, _, _, Database = __construct_nodes__(db_config)
        self._tree = Tree(); self._tree.construct(Database, self._columns)
