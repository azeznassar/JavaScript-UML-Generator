from esprima import tokenize, parseScript


class JavascriptHandler():
    """Responsible for converting"""

    def __init__(self, the_js : str, current_cmd : str):
        self.js_code = the_js
        self.current_cmd = current_cmd

    # Azez method's
    def extract_javascript_a(self):
        """ 1 """

    def create_puml_a(self):
        """ 1 """

    # Ethan method's
    def extract_javascript_b(self):
        #tokenize(self.js_code)
        return parseScript(self.js_code)

    def create_puml_b(self):
        """ 1 """

    # Shared method's
    