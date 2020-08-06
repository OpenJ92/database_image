from src.connect.dispatcher import connect
from src.struct.tree import Tree
from src.objects.database import Database

from pandas import read_sql

class Context(object):
    def __init__(self, database, name, config):
        self._connection = connect(database, name, config).connection
        with self._connection as conn:
            self._columns =\
                    read_sql("select * from information_schema.columns",conn)

        self._tree = Tree(); self._tree.construct(Database, self._columns)
