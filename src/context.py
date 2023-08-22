from src.connect.dispatcher import connect
from src.struct.tree import Tree
from src.struct.graph import Graph
from src.objects.dynamicnodes import __construct_nodes__

from pandas import read_sql

class Context(object):
    def __init__(self, database, name, config):
        """
        __init__ (str, str, str)
        User passes:
            database :: String - Database Object name from src.database.*
            name :: String - Name of database on which context is queried.
            config :: String - File with appriproate parameters to 'database' connect
                                function.
        """

        ## With dispatch connector, construct connection object to specified database.
        ## (Database a) => connect -> a
        self._connection = connect(database, name, config).connection

        with self._connection as conn:
            ## read in schema tree query for _connection database object. Execute query and store into
            ## self._columns.
            self._columns =\
                    read_sql(self._connection.information_schema_tree, conn)

            ## read in schema graph query for _connection database object. Execute query and store into
            ## self._edgees. (Construction of DAG of given database.)
            self._edges =\
                    read_sql(self._connection.information_schema_graph, conn)


        ## Construct database Column, Table, Schema, Database objects given _connection object.
        ## See src/objects/dynamic_nodes.py for more details.
        Column, Table, Schema, Database = __construct_nodes__(self._connection)

        self._tree = Tree();
        self._tree.construct(Database, name, self._columns)

        tables = {};
        self._tree.collect_tables(self._tree._root, tables)
        self._graph = Graph();
        self._graph.construct(tables, self._edges)
