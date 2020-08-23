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
        my_ast = parseScript(self.js_code)
        my_classes = []
        overall_class_attributes = []
        count = 0

        for a_class in my_ast.body:

            current_class = {
                "class_name": "",
                "class_attributes": [],
                "class_methods": []
            }

            current_class["class_name"] = a_class.id.name

            #my_classes.append(a_class.id.name)
            my_methods = my_ast.body[count].body.body
            #my_attributes = my_ast.body[count].body.body[count]

            current_class_methods = []
            current_class_attributes = []
            count = count + 1

            for method in my_methods:
                if method.key.name == "constructor":
                    for e in method.value.body.body:
                        if e.expression.left.object.type == "ThisExpression":
                            current_attribute = e.expression.left.property.name
                            current_class_attributes.append(current_attribute)
                    current_class["class_attributes"] = current_class_attributes
                    overall_class_attributes.append(current_class_attributes)
                current_class_methods.append(method.key.name)
            current_class["class_methods"] = current_class_methods
            #overall_class_methods.append(current_class_methods)
            my_classes.append(current_class)



        #current_class_attributes = my_ast.body[0].body.body[0].value.body.body[0].expression.left.object.type #.value.params

        #my_methods = my_ast.body[0].body.body
        #current_class_methods = []

        #my_data = my_classes, overall_class_methods, overall_class_attributes
        return my_classes #current_class_attributes #my_classes, current_class_methods

   

    # Ethan method's
    def extract_javascript_b(self):
        #tokenize(self.js_code)
        self.js_code = parseScript(self.js_code)


    # Shared method's
    
    def create_puml(self):
        my_dot_formatter = DotFormatter(self.js_code)
        if self.current_cmd == "a":
            my_dot_formatter.convert_to_dot_a()
        else:
            my_dot_formatter.convert_to_dot_b()

            
        my_dot_formatter.handle_dot_file(self.current_cmd)
