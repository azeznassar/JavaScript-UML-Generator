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

#blahh = CurrentCMD_B()
#blahh.cmdloop()
