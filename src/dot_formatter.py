# pylint: disable="import-error"
from image_converter import ImageConverter
from graphviz import Digraph
import os

class DotFormatter():

    def __init__(self, new_js):
        self.js_ast = new_js
    
    def convert_to_dot_a(self):
        os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz/bin/'
        js_data = self.js_ast
        dot = Digraph(name="G", node_attr={'shape' : 'record'}, format="png")
        #count = 0 
        for a_class in js_data:
            #dot.node('Animal', '{Animal|+ name : string\l+ age : int\l|+ die() : void\l}') 
            current_class = a_class.get("class_name")
            current_class_attributes = a_class.get("class_attributes")
            current_class_methods = a_class.get("class_methods")

            current_class_label = '{' + current_class + '| '
            for attribute in current_class_attributes:
                current_class_label += f'{attribute} : string\l '

            current_class_label += "| "

            for method in current_class_methods:
                current_class_label += method + "() : void\l"

            current_class_label += "}"
            #current_class_label += "| method1() : void\l}"

            dot.node(current_class, current_class_label) 
        
        dot.render("test") 

        # with open("dot.txt", 'w') as d:
        #     d.truncate()
        #     d.write(dot.source)
        #js_data = self.js_ast
        # with open("boilerplate.txt", 'r') as b:
        #     #d.truncate()
        #     boilerplate = b.read()

        # with open("dot.txt", 'w') as d:
        #     d.truncate()
        #     d.write(boilerplate)
        #     d.write("""
        #         Building [
        #                 label = "{Building|+ name : string\l+ age : int\l|+ die() : void\l}"
        #         ]

        #         Library [
        #                 label = "{Library||+ bark() : void\l}"
        #         ]

        #         House [
        #                 label = "{House||+ meow() : void\l}"
        #         ]
        #     }    
        #     """)

    def convert_to_dot_b(self):
        all_js_classes = self.js_ast
        dot_relationships = ''
        with open("boilerplate.txt", "r") as boiler_plate:
            dot_notation = boiler_plate.read()

        for a_class in all_js_classes:
            all_attributes = ''
            all_methods = ''
            all_relationships = ''

            for a_attribute, a_attribute_type in zip(a_class["attributes"], a_class["attribute_types"]):
                all_attributes += "{0} {1} \l".format(a_attribute, a_attribute_type)
            
            for a_method in a_class["methods"]:
                all_parameters = ''
                for a_parameter in a_method["parameters"]:
                    all_parameters += f"{a_parameter}, "
                all_methods += '{0}({1}){2}\l'.format(a_method["name"], all_parameters, a_method["return_type"])

            for a_relationship in a_class["class_calls"]:
                all_relationships += f'{a_class["class_name"]} -> {a_relationship}\n'

            if a_class["inherits_from"] != "":
                all_relationships += f'{a_class["class_name"]} -> {a_class["inherits_from"]} [arrowhead = onormal]\n'
    
            class_notation = '{0} [ label = "{{ {0}| {1}| {2} }}" ]'.format(a_class["class_name"], all_attributes, all_methods)
            dot_notation += f'{class_notation}\n'
            dot_relationships += all_relationships
        
        dot_notation += f"{dot_relationships} \n }}"
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

