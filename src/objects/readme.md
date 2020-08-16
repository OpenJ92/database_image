## Objects

Objects are dynamically constructed Nodes provided a database implementation. Once constructed, they are instanciated over the database through a parsing of the information_schema.columns view. an example Node materialized should look like the following.

``` python
class Schema(Node, object):
    def __getitem__(self, item):
        return self._children[item]

    def __iter__(self):
        for col, con in self._children.items():
            yield col, con

    def __init__(self, parent, name, data):
    	Node.__init__(self, parent, name)
    	self._children = self._construct_children(data)

    def _construct_children(self, data):
        unique_children = data[__db__.db_isconfig[__type__.__name__]].unique()
        return \
                {
                    elmt
                    :
		    ## __db__ variable corresponds to a class inheriting from ABC database in ./src/database
                    Table(self, elmt, data[data[__db__.db_isconfig[__type__.__name__]] == elmt])
                    for elmt in unique_children
                    if elmt not in __db__.restrict['Table']
                }

class Tree(object):
    def construct(self, __type__, name, data):
        self._root = __type__(None, name, data)

    def collect_tables(self, node, dictionary):
        if type(node).__name__ == 'Table':
            dictionary[node._parent._name + '.' + node._name] = node
        else:
            for _, child in node._children.items():
                self.collect_tables(child, dictionary)
```
