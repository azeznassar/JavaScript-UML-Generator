# pylint: disable="import-error"
from image_converter import ImageConverter

class DotFormatter():

    def __init__(self, new_js):
        self.js_ast = new_js
    
    def convert_to_dot_a(self):
        pass

    def convert_to_dot_b(self):
        dot_language = """
            digraph G {
                fontname = "Bitstream Vera Sans"
                fontsize = 20

                node [
                        fontname = "Bitstream Vera Sans"
                        fontsize = 10
                        shape = "record"
                ]

                edge [
                        fontname = "Bitstream Vera Sans"
                        fontsize = 8
                ]

                Fish [
                        label = "{Fish|+ name : string\l+ age : int\l|+ die() : void\l}"
                ]

                SeaDog [
                        label = "{SeaDog||+ bark() : void\l}"
                ]

                SeaLion [
                        label = "{SeaLion||+ meow() : void\l}"
                ]
            }
        """
        with open("dot.txt", 'w') as dot_file:
            dot_file.truncate()
            dot_file.write(dot_language)

    # Shared Methods
    def handle_dot_file(self, current_cmd):
        the_image_converter = ImageConverter()

        if current_cmd == "a":
            the_image_converter.produce_image_a()
        else:
            the_image_converter.produce_image_b()

