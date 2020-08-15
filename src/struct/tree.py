import enum
class Color(enum.Enum):
    black = 0; gray = 1; white = 2;

class Node(object):
    def __init__(self, parent, name, data = None, information = None, color = Color.black):
        self._information = information
        self._color = color
        self._name = name
        self._parent = parent
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
    def __construct_children__(cls, __type__, __db__):
        def _construct_children(self, data):
            unique_children = data[__db__.db_isconfig[__type__.__name__]].unique()
            return \
                    {
                        elmt
                        :
                        __type__(self, elmt, data[data[__db__.db_isconfig[__type__.__name__]] == elmt])
                        for elmt in unique_children
                        if elmt not in __db__.restrict[__type__.__name__]
                    }
        return _construct_children

class Tree(object):
    def construct(self, __type__, name, data):
        self._root = __type__(None, name, data)
