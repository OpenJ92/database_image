from abc import ABCMeta, abstractmethod

class database(metaclass = ABCMeta):
    @abstractmethod
    def get_information_schema_tree(self):
        pass

    @abstractmethod
    def get_information_schema_graph(self):
        pass
