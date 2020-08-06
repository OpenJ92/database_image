from src.objects.column import Column
from src.struct.tree import Node

class Table(Node):
    def __init__(self, parent, name, data):
        Node.__init__(self, parent, name)
        self._children = self._construct_children(data)

    def _construct_children(self, data):
        return self.__construct_children__(Column, 'column_name')(data)

