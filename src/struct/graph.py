class GNode(object):
    def __init__(self, table, column):
        self._table = table
        self._column = column

class Adjlists(object):
    def __init__(self):
        pass

class Adjlist(object):
    def __init__(self):
        pass

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
            self._adjlist[tables[prim]].append(GNode(tables[fore], tables[fore][key]))
