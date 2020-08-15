import enum
class Color(enum.Enum):
    black = 0; gray = 1; white = 2;

class GNode(object):
    def __init__(self, table, column, color = Color.black):
        self._table = table
        self._column = column
        self._color = color

class Graph(object):
    def __init__(self):
        self._vcount = 0
        self._ecount = 0

        self._adjlist = {}

    def construct(self, tables, data):
        for _, table in tables.items():
            self._adjlist[table] = []

        collect_relations = \
                list(zip(list(data['primary_table']), list(data['foreign_table']), list(data['fk_columns'])))

        for prim, fore, key in collect_relations:
            self._adjlist[tables[prim]].append(GNode(tables[prim], tables[fore][key]))
