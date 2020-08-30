
from esprima import tokenize, parseScript
from dot_formatter import DotFormatter


class JavascriptHandler():
    """Responsible for converting"""

    def __init__(self, the_js: str, current_cmd: str):
        self.js_code = the_js
        self.current_cmd = current_cmd

    # Azez method's
    def extract_javascript_a(self):
        """ 1 """
        my_ast = parseScript(self.js_code)
        # print(my_ast)
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
                "class_method_params": {},  # MAKE INTO DICT
                "class_associations": [],
                "class_parent": ""
            }

            current_class["class_name"] = a_class.id.name

            # my_classes.append(a_class.id.name)
            my_methods = my_ast.body[count].body.body
            # my_attributes = my_ast.body[count].body.body[count]

            current_class_methods = []
            current_class_method_return_values = []
            current_class_method_params = {}
            current_class_attributes = []
            current_class_attribute_values = []
            current_class_associations = []

            count = count + 1
            method_count = 0

            if a_class.superClass != None:
                current_class["class_parent"] = a_class.superClass.name
                # print(current_class["class_parent"])

            for method in my_methods:
                current_method_value = ""
                # if method.key.name == "constructor":

                for e in method.value.body.body:

                    if method.key.name == "constructor":

                        if e.expression.left.object.type == "ThisExpression":
                            current_attribute = e.expression.left.property.name
                            current_attribute_value = e.expression.right.value
                            current_class_attributes.append(current_attribute)
                            current_class_attribute_values.append(
                                current_attribute_value)

                    is_var = e.type == "VariableDeclaration"
                    if is_var and e.declarations[0].init.type == "NewExpression":
                        current_class["class_associations"].append(
                            e.declarations[0].init.callee.name)

                    if e.expression != None:
                        if e.expression.right != None:
                            # print(e.expression.right)
                            if e.expression.right.type == "NewExpression":
                                # print(e.expression.right.callee.name)
                                current_class["class_associations"].append(
                                    e.expression.right.callee.name)

                current_class["class_attributes"] = current_class_attributes
                current_class["class_attribute_values"] = current_class_attribute_values
                current_class["class_associations"] = current_class_associations
                overall_class_attributes.append(current_class_attributes)

                current_class_methods.append(method.key.name)
                # if method.value.params != []:
                current_params = method.value.params
                # print(current_params)
                # empty_list = []
                # if current_params != empty_list:
                # if method.key.name != "constructor":
                current_class_method_params[f'{method.key.name}'] = []
                for p in current_params:
                    # param = p.name
                    # print(p.name)
                    # print(method.key.name)

                    current_class_method_params[f'{method.key.name}'].append(
                        p.name)

                method_count = method_count + 1

                for e in method.value.body.body:

                    if e.type == "ReturnStatement":
                        current_method_value = type(e.argument.value).__name__

                    if current_method_value == "":
                        current_method_value = "void"
                # print(current_method_value)
                current_class_method_return_values.append(current_method_value)

            current_class["class_methods"] = current_class_methods
            current_class["class_method_values"] = current_class_method_return_values
            # print(current_class_method_params)
            current_class["class_method_params"] = current_class_method_params
            # overall_class_methods.append(current_class_methods)
            my_classes.append(current_class)
    
        self.js_code = my_classes

    # Ethan method's
    def extract_javascript_b(self):
        js_ast = parseScript(self.js_code)

        all_js_classes = []

        for a_class in js_ast.body:
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
                    new_method = {"name": "",
                                  "parameters": [], "return_type": ""}

                    if a_method.type == "MethodDefinition":
                        new_method["name"] = a_method.key.name
                        for a_param in a_method.value.params:
                            new_method["parameters"].append(a_param.name)

                    for an_expression in a_method.value.body.body:

                        if an_expression.type == "ReturnStatement":
                            new_method["return_type"] = f' : {type(an_expression.argument.value).__name__}'

                        e_type = an_expression.type == "VariableDeclaration"
                        if e_type and an_expression.declarations[0].init.type == "NewExpression":
                            class_dict["class_calls"].append(
                                an_expression.declarations[0].init.callee.name)

                        if an_expression.expression != None:
                            left_value = an_expression.expression.left
                            right_value = an_expression.expression.right

                            if a_method.key.name == "constructor":  # Grab Attributes of constructor
                                if left_value.object.type == "ThisExpression":
                                    class_dict["attributes"].append(
                                        left_value.property.name)
                                    # Grabs attribute types - Gives empty string if no type value given
                                    attribute_value = right_value.value
                                    if isinstance(attribute_value, type(None)):
                                        value_type = ""
                                    else:
                                        value_type = f' : {type(attribute_value).__name__}'
                                    class_dict["attribute_types"].append(
                                        value_type)

                            if right_value != None and right_value.type == "NewExpression":
                                class_dict["class_calls"].append(
                                    right_value.callee.name)
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
