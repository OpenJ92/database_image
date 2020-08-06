import enum
class Color(enum.Enum):
    black = 0; gray = 1; white = 2;

class Node(object):
    def __init__(self, parent, name, information = None, color = Color.black):
        self._information = information
        self._color = color
        self._name = name
        self._parent = parent
        self._children = {}

    def __getitem__(self, item):
        return self._children[item]

    def __construct_children__(self, __type__, __db__):
        def _construct_children(data):
            unique_children = data[__db__].unique()
            return \
                    {
                        elmt
                        :
                        __type__(self, elmt, data[data[__db__] == elmt])
                        for elmt in unique_children
                    }
        return _construct_children

class Tree(object):
    def construct(self, _type, data):
        self._root = _type(None, _type.__name__, data)

    def print_(self):
        self._root.print_()
