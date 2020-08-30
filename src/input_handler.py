
# Input Handler

# pylint: disable="import-error"
from current_cmd_a import CurrentCMD_A
from current_cmd_b import CurrentCMD_B
from javascript_handler import JavascriptHandler
# 3rd party imports
from serializer import Serializer
from esprima import tokenize, parseScript
from plantuml import PlantUML
from re import search
from os import walk, path
from execjs import get

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""
  
  def __init__(self):
    self.cmd_a = CurrentCMD_A()
    self.cmd_b = CurrentCMD_B()
    # self.all_javascript = str

  #Ethan's 
  def is_file_or_dir_b(self, input: str):
    if path.isfile(input):
      if search(".js$", input) != None:
        my_js_file = [input]
        return self.validate_javascript_b(my_js_file)

    elif path.isdir(input):
      all_js_files = []
      for subdir, dirs, files in walk(input):
        for f in files:
          a_file = f'{subdir}\\{f}'
          if search(".js$", a_file) != None:
            all_js_files.append(a_file)
      return self.validate_javascript_b(all_js_files)
   
  def validate_javascript_b(self, js_file_list):
    node_runner = get('Node')
    
    for a_single_file in js_file_list:
      javascript_program = node_runner.compile('''
          module.paths.push('%s');
          standard_package = require('standard');

          function validateMyJS() {
            return standard_package.lintTextSync('%s')
          }

      ''' % (path.join(path.dirname(__file__),'node_modules') , a_single_file))

      standard_data = javascript_program.call('validateMyJS')

      if standard_data['results'][0]['messages'] != None:
        for error in standard_data['results'][0]['messages']:
          print("Error Located: " + error['message'])

      print(f"Error Count: {standard_data['errorCount']}")
      print(f"Warning Count: {standard_data['warningCount']} \n")

    all_javascript_string = ""
    for a_file in js_file_list:
      with open(a_file) as js_file:
        js_code = js_file.read()
        all_javascript_string += f"{js_code}\n"

    print("Files Have been Validated by Standard JS \n")
    return all_javascript_string

  #Azez's 
  def is_file_or_dir_a(self, user_input):
    is_file = path.isfile(user_input)
    is_dir = path.isdir(user_input)

    if is_file:
      if search(".js$", user_input) != None:
        return self.validate_javascript_a([user_input])

    elif is_dir:
      js_files = []
      for subdir, dirs, files in walk(user_input):
        for f in files:
          current_file = subdir + "\\" + f
          if search(".js$", current_file) != None:
            js_files.append(current_file)
      return self.validate_javascript_a(js_files)

  def validate_javascript_a(self, js_files):
    runtime = get('Node')

    print("Validating JavaScript file(s)")
    for current_file in js_files:
      context = runtime.compile('''
          module.paths.push('%s');
          s = require('standard');

          function lintJS() {
            return s.lintTextSync('%s')
          }

      ''' % (path.join(path.dirname(__file__),'node_modules') , current_file))

      validation_results = context.call('lintJS')
      error_count = validation_results['errorCount']
      warning_count = validation_results['warningCount']

      if validation_results['results'][0]['messages'] != None:
        error_messages = validation_results['results'][0]['messages']
        for error in error_messages:
          print("Error Found.")
          print("Error Message: " + error['message'])

      print("Error Count: " + str(error_count))
      print("Warning Count: " + str(warning_count) + '\n')

    js_code = ""
    for f in js_files:
      with open(f) as js_file:
        js = js_file.read()
        js_code += js + ' \n'

    return js_code

  #Shared methods 
  def handle_javascript(self, js : str, current_cmd : str):
    "Creates a javascript handler for given set of javascript file(s)"

    my_javascript = JavascriptHandler(js, current_cmd)
    my_serializer = Serializer()

    if current_cmd == "a":
      my_javascript.extract_javascript_a()
      my_serializer.serialize_a(my_javascript.js_code)
    else:
      my_javascript.extract_javascript_b()
      my_serializer.serialize_b(my_javascript.js_code)

    my_javascript.create_puml()

  def cmd_looper(self, current_cmd, output):
    current_cmd.cmdloop(intro = output)

    user_command = current_cmd.current_command
    is_ethans = current_cmd == input_handler.cmd_b
    #is_azezs = current_cmd == input_handler.cmd_b

    # CMD Switcher
    if user_command == "do_switch_cmd":
      if is_ethans:
        current_cmd = input_handler.cmd_a
      else:
        current_cmd = input_handler.cmd_b
      current_cmd.current_command = ""
      self.cmd_looper(current_cmd, "CMD Switched")

    # JS file checker
    if user_command == "do_create_uml":
      current_cmd.current_command = ""
      if is_ethans:
        my_data = self.is_file_or_dir_b(current_cmd.user_args)
        self.handle_javascript(my_data, "b")
      else:
        my_data = self.is_file_or_dir_a(current_cmd.user_args)
        self.handle_javascript(my_data, "a")
      
      self.cmd_looper(current_cmd, "UML Diagram generated ./uml.png")

    if user_command == "do_deserialize":
      my_serializer = Serializer() # WRAP in try / catch
      deserialize_args = current_cmd.user_args
      if is_ethans:
        my_serializer.deserializer_b(deserialize_args)
      else:
        my_serializer.deserializer_a(deserialize_args)

      self.cmd_looper(current_cmd, "deserialized data has been printed \n")

    # Quitter
    if user_command == "do_quit":
      return

if __name__ == "__main__":
  import sys
  input_handler = InputHandler()
  current_cmd = input_handler.cmd_b # Default CMD is Ethan's
  # print(sys.argv[0]) # src\input_handler.py 0 or 1
  if len(sys.argv) > 1:
    if sys.argv[1] == "0":
      input_handler.cmd_looper(input_handler.cmd_a, "Running Azez's cmd") # Azez CMD
    if sys.argv[1] == "1":
      input_handler.cmd_looper(input_handler.cmd_b, "Running Ethan's cmd") # Ethan CMD

  input_handler.cmd_looper(current_cmd, "Running Ethan's cmd")


    



  
    


    
