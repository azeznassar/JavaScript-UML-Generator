# pylint: disable="import-error"
from image_converter import ImageConverter

class DotFormatter():

    def __init__(self, new_js):
        self.js_ast = new_js
    
    def convert_to_dot_a(self):
        current_ast = self.js_ast
        current_class = current_ast.body[0].id.name
        #current_attribute = current_ast.body[0].id.
        # #DONT NEED TO WORRY ABOUT CONSTRCUTOR, JUST GET ATTRIB NAMES/types - then get method names.
        #current_attribute_type
        #current_method
        return current_class

    def convert_to_dot_b(self):
        module_name = self.js_ast.body[0]
        class_name = module_name.id.name
        return class_name
        



    # Shared Methods

    def handle_dot_file(self, current_cmd):
        the_image_converter = ImageConverter()

        if current_cmd == "a":
            the_image_converter.produce_image_a()
        else:
            the_image_converter.produce_image_b()

