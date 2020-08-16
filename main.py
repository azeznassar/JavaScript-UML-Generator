from esprima import tokenize, parseScript

code = 'const my_string = "hello world"'
tokenize(code)
print(parseScript(code))