from src.struct.tree import Node

class Column(Node):
    def __init__(self, parent, name, data):
        Node.__init__(self, parent, name)
        self._data = data
        self._children = self._construct_children(data)

    def _construct_children(self, data):
        return None
