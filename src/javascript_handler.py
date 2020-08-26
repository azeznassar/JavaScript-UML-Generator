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
                "class_attribute_values": [],
                "class_methods": [],
                "class_method_values": [],
                "class_method_params": [],
                "class_associations": []
            }

            current_class["class_name"] = a_class.id.name

            #my_classes.append(a_class.id.name)
            my_methods = my_ast.body[count].body.body
            #my_attributes = my_ast.body[count].body.body[count]

            current_class_methods = []
            current_class_method_return_values = []
            current_class_method_params = []
            current_class_attributes = []
            current_class_attribute_values = []
            current_class_associations = []
            count = count + 1
            method_count = 0
            for method in my_methods:

                #if method.key.name == "constructor":

            
                for e in method.value.body.body:

                    if method.key.name == "constructor":

                        if e.expression.left.object.type == "ThisExpression":
                            current_attribute = e.expression.left.property.name
                            current_attribute_value = e.expression.right.value
                            current_class_attributes.append(current_attribute)
                            current_class_attribute_values.append(current_attribute_value)


                    elif type(e.expression.right) != type(None) and e.expression.right.type == "NewExpression":
                        #print(e.expression.right.callee.name)
                        current_class["class_associations"].append(e.expression.right.callee.name)

                current_class["class_attributes"] = current_class_attributes
                current_class["class_attribute_values"] = current_class_attribute_values
                current_class["class_associations"] = current_class_associations
                overall_class_attributes.append(current_class_attributes)

                current_class_methods.append(method.key.name)
                #if method.value.params != []:
                current_params = method.value.params
                #empty_list = []
                #if current_params != empty_list:
                for p in current_params: 
                    #param = p.name
                #print(p.name)
                    current_class_method_params.append(p.name) # Need to link params with specific method, instead of generic to the class

                method_count = method_count + 1
                for e in method.value.body.body:
                    if e.type == "ReturnStatement":
                        current_method_value = e.argument.value
                        current_class_method_return_values.append(current_method_value)

 

                current_class["class_methods"] = current_class_methods
                current_class["class_method_values"] = current_class_method_return_values
                current_class["class_method_params"] = current_class_method_params
                #overall_class_methods.append(current_class_methods)
            my_classes.append(current_class)



        #current_class_attributes = my_ast.body[0].body.body[0].value.body.body[0].expression.left.object.type #.value.params

        #my_methods = my_ast.body[0].body.body
        #current_class_methods = []

        #my_data = my_classes, overall_class_methods, overall_class_attributes
        #return my_classes #current_class_attributes #my_classes, current_class_methods
        self.js_code = my_classes
        #return my_classes

    # Ethan method's
    def extract_javascript_b(self):
        js_ast = parseScript(self.js_code)

        all_js_classes = []

        for a_class in js_ast.body: # Where my_javascript is what esprima parses
            class_dict = {"class_name": "",
                        "attributes": [],
                        "methods": []}

            if a_class.type == "ClassDeclaration":
                class_dict["class_name"] = a_class.id.name
                
                for a_method in a_class.body.body:

                    if a_method.key.name == "constructor": # Grab Attributes of constructor                
                        for an_expression in a_method.value.body.body:
                            if an_expression.expression.left.object.type == "ThisExpression":
                                class_dict["attributes"].append(an_expression.expression.left.property.name)
                            
                    if a_method.type == "MethodDefinition":
                        class_dict["methods"].append(a_method.key.name)
            
            all_js_classes.append(class_dict)

        self.js_code = all_js_classes


    # Shared method's

    def create_puml(self):
        my_dot_formatter = DotFormatter(self.js_code)
        if self.current_cmd == "a":
            my_dot_formatter.convert_to_dot_a()
        else:
            my_dot_formatter.convert_to_dot_b()

            
        my_dot_formatter.handle_dot_file(self.current_cmd)
