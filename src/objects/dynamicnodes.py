from src.struct.tree import Node

def __construct_nodes__(db):

    ## Move Node function constructors into Factory Class...
    c_children = None
    c_init = Node.__construct_init__(c_children)
    Column = type('Column', (Node,), {'__init__':c_init,'_construct_children':c_children})

    t_children = Node.__construct_children__(Column, db)
    t_init = Node.__construct_init__(t_children)
    Table = type('Table', (Node,), {'__init__':t_init,'_construct_children':t_children})

    s_children = Node.__construct_children__(Table, db)
    s_init = Node.__construct_init__(s_children)
    Schema = type('Schema', (Node,), {'__init__':s_init,'_construct_children':s_children})

    d_children = Node.__construct_children__(Schema, db)
    d_init = Node.__construct_init__(d_children)
    Database = type('Database', (Node,), {'__init__':d_init,'_construct_children':d_children})

    return Column, Table, Schema, Database
