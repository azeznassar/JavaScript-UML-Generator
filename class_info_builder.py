from abc import ABC, abstractmethod

class classInfoBuilder(ABC):
    def __init__(self):
        self.result = { }

    def get_result(self):
        return self.result

    @abstractmethod
    def add_class_name(self, name):
        pass

    @abstractmethod
    def add_class_attributes_types(self, attrib):
        pass

    @abstractmethod
    def add_class_attribute_values(self, value):
        pass

    @abstractmethod
    def add_class_methods(self, method):
        pass

    @abstractmethod
    def add_class_parents(self, parents):
        pass

    @abstractmethod
    def add_class_associations(self, associations):
        pass

