from esprima import tokenize, parseScript
from dot_formatter import DotFormatter

class JavascriptHandler():
    """Responsible for converting"""

    def __init__(self, the_js : str, current_cmd : str):
        self.js_code = the_js
        self.current_cmd = current_cmd

    # Azez method's
    def extract_javascript_a(self):
        """ 1 """

   

    # Ethan method's
    def extract_javascript_b(self):
        #tokenize(self.js_code)
        return parseScript(self.js_code)


    # Shared method's
    
    def create_puml(self):
        my_dot_formatter = DotFormatter(self.js_code)
        if self.current_cmd == "a":
            my_dot_formatter.convert_to_dot_a()
        else:
            my_dot_formatter.convert_to_dot_b()

            
        my_dot_formatter.handle_dot_file(self.current_cmd)
        