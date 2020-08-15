class GNode(object):
    def __init__(self, table, column):
        pass

class AdjList(object):
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

        collect_relations = list(zip(list(data['primary_table']), list(data['foreign_table'])))

        for prim, fore in collect_relations:
            try:
                ## replace these table appends with GNode appends
                ## so we can carry along the foreign key in the
                ## target node. Do we want these to be directed
                ## or undirected?
                self._adjlist[tables[prim]].append(tables[fore])
                self._adjlist[tables[fore]].append(tables[prim])
            except KeyError:
                self._adjlist[tables[prim]] = [tables[fore]]
