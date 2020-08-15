from src.connect.dispatcher import connect
from src.struct.tree import Tree
from src.objects.dynamicnodes import __construct_nodes__

from pandas import read_sql

class Context(object):
    def __init__(self, database, name, config):
        self._connection = connect(database, name, config).connection

        with self._connection as conn:
            self._columns =\
                    read_sql(self._connection.information_schema_tree,conn)

            self._edges =\
                    read_sql(self._connection.information_schema_graph, conn)

        Column, Table, Schema, Database = __construct_nodes__(self._connection)
        self._tree = Tree(); self._tree.construct(Database, name, self._columns)
