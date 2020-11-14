# pylint: disable="import-error"
from class_info_builder import classInfoBuilder

class ClassInfoBuilderA(classInfoBuilder):
    def __init__(self):
        self.result = {
                "class_name": "",
                "class_attributes": [],
                "class_attribute_values": [],
                "class_methods": [],
                "class_method_values": [],
                "class_method_params": {},
                "class_associations": [],
                "class_parent": ""
            }

    def add_class_name(self, name):
        self.result["class_name"] = name

    def add_class_attributes_types(self, attrib):
        self.result["class_attributes"] = attrib

    def add_class_attribute_values(self, value):
        self.result["class_attribute_values"] = value

    def add_class_methods(self, method):
        self.result["class_methods"] = method["methods"]
        self.result["class_method_values"] = method["values"]
        self.result["class_method_params"] = method["params"]

    def add_class_parents(self, parents):
        self.result["class_parent"] = parents

    def add_class_associations(self, associations):
        self.result["class_associations"] = associations

# {
#                 "class_name": "",
#                 "class_attributes": [],
#                 "class_attribute_values": [],
#                 "class_methods": [],
#                 "class_method_values": [],
#                 "class_method_params": {},  # MAKE INTO DICT
#                 "class_associations": [],
#                 "class_parent": ""
#             }