# pylint: disable="import-error"
from class_info_builder import classInfoBuilder

class ClassInfoBuilderB(classInfoBuilder):
    def __init__(self):
        self.result = {"class_name": "",
                       "attributes": [],
                       "attribute_types": [],
                       "methods": [],
                       "class_calls": [],
                       "inherits_from": ""}

    def add_class_name(self, name):
        self.result["class_name"] = name

    def add_class_attributes_types(self, attrib):
        self.result["attribute_types"] = attrib

    def add_class_attribute_values(self, value):
        self.result["attributes"] = value

    def add_class_methods(self, method):
        self.result["methods"] = method

    def add_class_parents(self, parents):
        self.result["inherits_from"] = parents

    def add_class_associations(self, associations):
        self.result["class_calls"] = associations

