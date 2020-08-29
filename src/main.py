#Testing/Prototyping module

from esprima import tokenize, parseScript
from plantuml import PlantUML
from current_cmd_a import CurrentCMD_A
from current_cmd_b import CurrentCMD_B
import ast

pl = PlantUML(url='http://www.plantuml.com/plantuml/img/')

code = """
class Cat {
  constructor(name) {
    this.name = name;
  }
  
  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}
"""
#tokenize(code)
#my_ast = parseScript(code)
#new_code = ast.parse(my_ast, mode='eval')
#print(eval(compile(new_code, '', mode='eval')))
#pl.processes_file("test.txt")

#current_cmd = CurrentCMD_B()

all_js_classes = []


with open("test.js", 'r') as js_file:
  js_ast = js_file.read()
  js_ast = parseScript(js_ast)


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
