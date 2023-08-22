import enum
class Color(enum.Enum):
    black = 0; gray = 1; white = 2;

class Node(object):
    def __init__(self, parent, name, data = None, information = None, color = Color.black):
        self._information = information
        self._name = name
        self._parent = parent
        self._color = color
        self._children = {}

    def __getitem__(self, item):
        return self._children[item]

    def __iter__(self):
        for col, con in self._children.items():
            yield col, con

    @classmethod
    def __construct_init__(cls, _construct_children):
        def __init__(self, parent, name, data):
            Node.__init__(self, parent, name)
            self._children = dict(zip(list(data.columns), list(*data.values))) \
                             if not _construct_children                        \
                             else self._construct_children(data)
        return __init__


    @classmethod
    def __construct_children__(cls, typ, db):
        def _construct_children(self, data):
            unique_children = data[db.infoconfig[typ.__name__]].unique()
            return \
                    {
                        elmt
                        :
                        typ(self, elmt, data[data[db.infoconfig[typ.__name__]] == elmt])
                        for elmt in unique_children
                        if elmt not in db.restrict[typ.__name__]
                    }
        return _construct_children


class Tree(object):
    def construct(self, typ, name, data):
        self._root = typ(None, name, data)

    def collect_tables(self, node = None, dictionary = {}):
        if not node: node = self._root

        if type(node).__name__ == 'Table':
            dictionary[node._parent._name + '.' + node._name] = node
        else:
            for _, child in node._children.items():
                self.collect_tables(child, dictionary)
