from src.struct.tree import Node

def construct_node(name, __type__, __db__):

    def __init__(s, parent, name, data):
        Node.__init__(s, parent, name)
        s._children = s._construct_children(data)

    def _construct_children(self, data):
        return self.__construct_children__(__type__, __db__)(data)

    attrs = {'__init__':__init__, '_construct_children':_construct_children}

    return type(name, (Node,), attrs)

def construct_db_nodes():
    class Column(Node):
        def __init__(self, parent, name, data):
            Node.__init__(self, parent, name)
            self._data = data
            self._children = self._construct_children(data)

        def _construct_children(self, data):
            return None

    Table = construct_node('Table',Column,'column_name')
    Schema = construct_node('Schema',Table,'table_name')
    Database = construct_node('Database',Schema,'table_schema')

    return Column, Table, Schema, Database
