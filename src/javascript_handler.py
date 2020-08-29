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
                        "attribute_types": [],
                        "methods": [],
                        "class_calls": [],
                        "inherits_from": ""}

            if a_class.type == "ClassDeclaration":
                class_dict["class_name"] = a_class.id.name

                if a_class.superClass != None:
                    class_dict["inherits_from"] = a_class.superClass.name
                
                for a_method in a_class.body.body:
                    new_method = {"name" : "", "parameters": [], "return_type" : ""}

                    if a_method.type == "MethodDefinition": # if the type of expression is a method, add its name to methods array                    
                        new_method["name"] = a_method.key.name
                        for a_param in a_method.value.params:
                            new_method["parameters"].append(a_param.name)

                    for an_expression in a_method.value.body.body:

                        if an_expression.type == "ReturnStatement":
                                new_method["return_type"] = f' : {type(an_expression.argument.value).__name__}'
                        
                        if an_expression.expression != None:
                            left_value = an_expression.expression.left
                            right_value = an_expression.expression.right                         

                            if a_method.key.name == "constructor": # Grab Attributes of constructor
                                if left_value.object.type == "ThisExpression":
                                    class_dict["attributes"].append(left_value.property.name)
                                    # Grabs attribute types - Gives empty string if no type value given
                                    attribute_value = right_value.value
                                    if type(attribute_value) == type(None):
                                        value_type = ""
                                    else:
                                        value_type = f' : {type(attribute_value).__name__}'
                                    class_dict["attribute_types"].append(value_type)

                            if right_value.type == "NewExpression":
                                class_dict["class_calls"].append(right_value.callee.name)
                    class_dict["methods"].append(new_method)
            
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
