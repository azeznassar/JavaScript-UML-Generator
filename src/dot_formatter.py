# pylint: disable="import-error"
from image_converter import ImageConverter
from graphviz import Digraph

class DotFormatter():

    def __init__(self, new_js):
        self.js_ast = new_js
    
    def convert_to_dot_a(self):
        pass

    def convert_to_dot_b(self):
        all_js_classes = self.js_ast

        with open("boilerplate.txt", "r") as boiler_plate:
            dot_notation = boiler_plate.read()

        for a_class in all_js_classes:
            all_attributes = ''
            all_methods = ''
            for a_attribute in a_class["attributes"]:
                all_attributes += "{0}\l".format(a_attribute)

            for a_method in a_class["methods"]:
                all_methods += "{0}()\l".format(a_method)
    
            class_notation = '{0} [ label = "{{ {0}| {1}| {2} }}" ]'.format(a_class["class_name"], all_attributes, all_methods)
            dot_notation += f'{class_notation}\n'
        
        dot_notation += "\n }"
        with open("dot.txt", 'w') as dot_file:
            dot_file.truncate()
            dot_file.write(dot_notation)

    # Shared Methods
    def handle_dot_file(self, current_cmd):
        the_image_converter = ImageConverter()

        if current_cmd == "a":
            the_image_converter.produce_image_a()
        else:
            the_image_converter.produce_image_b()

