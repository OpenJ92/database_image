from src.struct.tree import Node

def __construct_nodes__(__db__):

    cconst = None
    Column = type('Column', (Node,), {'__init__':Node.__construct_init__(cconst),'_construct_children':cconst})

    tconst = Node.__construct_children__(Column, __db__['column'])
    Table = type('Table', (Node,), {'__init__':Node.__construct_init__(tconst),'_construct_children':tconst})

    sconst = Node.__construct_children__(Table, __db__['table'])
    Schema = type('Schema', (Node,), {'__init__':Node.__construct_init__(sconst),'_construct_children':sconst})

    dconst = Node.__construct_children__(Schema, __db__['schema'])
    Database = type('Database', (Node,), {'__init__':Node.__construct_init__(dconst),'_construct_children':dconst})

    return Column, Table, Schema, Database
