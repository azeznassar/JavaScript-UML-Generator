class ClassDirector:
    def __init__(self, builder):
        self.current_builder = builder

    def construct(self, input):
        self.current_builder.add_class_name(input["name"])
        self.current_builder.add_class_attributes_types(input["attribute_types"])
        self.current_builder.add_class_attribute_values(input["attribute_values"])
        self.current_builder.add_class_methods(input["method"])
        self.current_builder.add_class_parents(input["parent"])
        self.current_builder.add_class_associations(input["associations"])