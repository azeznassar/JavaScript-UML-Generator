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
#current_cmd = CurrentCMD_A()
#current_cmd.cmdloop()

my_ast = parseScript("""
class Cat {
    constructor(catName, catAge) {
      this.catName = 0;
      this.catAge = "";
    }
    
    speak() {
      console.log(`${this.catName} makes a noise.`);
    }

    displayAge() {
      console.log(`${this.catName} is ${this.catAge}.`);
    }
}

class Dog {
  constructor(dogName, dogAge) {
    this.dogName = dogName;
    this.dogAge = dogAge;
  }
  
  speak(myParam, myOtherParam) {
    console.log(`${this.dogName} makes a noise.`);

    return "thisisastring"
  }

  displayAge() {
    console.log(`${this.dogName} is ${this.dogAge}.`);

    return 19
  }
}
""")
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
           "class_method_params": []
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
  count = count + 1
  method_count = 0 
  for method in my_methods:
    if method.key.name == "constructor":
      for e in method.value.body.body:
        if e.expression.left.object.type == "ThisExpression":
          current_attribute = e.expression.left.property.name
          current_attribute_value = e.expression.right.value
          current_class_attributes.append(current_attribute)
          current_class_attribute_values.append(current_attribute_value)
      current_class["class_attributes"] = current_class_attributes
      current_class["class_attribute_values"] = current_class_attribute_values
      overall_class_attributes.append(current_class_attributes)

    current_class_methods.append(method.key.name)
    #if method.value.params != []:
    current_params = method.value.params
    #empty_list = []
    #if current_params != empty_list:
    for p in current_params:
        #param = p.name
      print(p.name)
      current_class_method_params.append(p.name)

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
print(my_classes)
#print(my_ast.body)
#print(my_ast.body[1].body.body.type) to do - params !