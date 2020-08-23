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

