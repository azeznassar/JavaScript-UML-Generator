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
        dot_notation = ""
        #dot = Digraph(name="G", node_attr={'shape' : 'round'}, format="png")
        #dot.node('Animal', '{Animal|+ name : string\l+ age : int\l|+ die() : void\l}') 
        #dot.node('Dog', '{Dog+ bark() : void\l}') 
        #dot.node('Cat', '{Cat+ meow() : void\l}')
        #dot_file.write(dot.source)


        for a_class in all_js_classes:
           class_notation = f'g' 

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

