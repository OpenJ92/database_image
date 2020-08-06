from src.objects.column import Column
from src.struct.tree import Node

## class Table(Node):
##     def __init__(self, parent, name, data):
##         Node.__init__(self, parent, name)
##         self._children = self._construct_children(data)
## 
##     def _construct_children(self, data):
##         return self.__construct_children__(Column, 'column_name')(data)


def construct_node(name, __type__, __db__):
    def __init__(s, parent, name, data):
        Node.__init__(s, parent, name)
        s._children = s._construct_children(data)
    def _construct_children(self, data):
        return self.__construct_children__(__type__, __db__)(data)
    attrs = {'__init__':__init__, '_construct_children':_construct_children}
    return type(name, (Node,), attrs)

Table = construct_node('Table', Column, 'column_name')
