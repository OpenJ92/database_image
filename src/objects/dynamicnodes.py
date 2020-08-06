from src.struct.tree import Node

def __construct_nodes__(__db__):

    def __co_init__(_construct_children):
        def __init__(self, parent, name, data):
            Node.__init__(self, parent, name)
            self._children = data.to_dict('list') if not _construct_children else _construct_children(data)
        return __init__

    cconst = None
    Column = type('Column', (Node,), {'__init__':__co_init__(cconst),'_construct_children':cconst})

    tconst = Node._construct_children_(Column, __db__['column'])
    Table = type('Table', (Node,), {'__init__':__co_init__(tconst),'_construct_children':tconst})

    sconst = Node._construct_children_(Table, __db__['table'])
    Schema = type('Schema', (Node,), {'__init__':__co_init__(sconst),'_construct_children':sconst})

    dconst = Node._construct_children_(Schema, __db__['schema'])
    Database = type('Database', (Node,), {'__init__':__co_init__(dconst),'_construct_children':dconst})

    return Column, Table, Schema, Database
