## Objects

Objects are dynamically constructed Nodes provided a [database implementation](https://github.com/OpenJ92/__dbm__/tree/master/src/database). Once constructed, they are instanciated over the database through a parsing of the information_schema.columns view over the [Tree and Graph](https://github.com/OpenJ92/__dbm__/tree/master/src/struct) datatypes. An example Node materialized should look like the following. Under no circumstance should a user edit these definitions unless s/he is looking to accumulate functionality by adding methods to the type namespaces in the dynamicnodes.py file.
 
``` python
class Schema(Node, object):
    ## inherited from node. 
    def __getitem__(self, item):
        return self._children[item]

    ## inherited from node. 
    def __iter__(self):
        for col, con in self._children.items():
            yield col, con

    def __init__(self, parent, name, data):
    	Node.__init__(self, parent, name)
    	self._children = self._construct_children(data)

    def _construct_children(self, data):
	## __db__ variable corresponds to a class inheriting from ABC database in [./src/database]()

        unique_children = data[__db__.db_isconfig[__type__.__name__]].unique()
        return \
                {
                    elmt
                    :
                    Table(self, elmt, data[data[__db__.db_isconfig[__type__.__name__]] == elmt])
                    for elmt in unique_children
                    if elmt not in __db__.restrict['Table']
                }
```
