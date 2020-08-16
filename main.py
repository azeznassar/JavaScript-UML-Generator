from esprima import tokenize, parseScript
from plantuml import PlantUML

pl = PlantUML(url='http://www.plantuml.com/plantuml/img/')

code = 'const my_string = "hello world"'
tokenize(code)
pl.processes_file("test.txt")