
# Input Handler
from esprima import tokenize, parseScript
from plantuml import PlantUML
# pylint: disable="import-error"
from current_cmd_a import CurrentCMD_A
from current_cmd_b import CurrentCMD_B

from javascript_handler import JavascriptHandler

#import ast
import re as regex

from os import walk, path

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""
  
  def __init__(self):
    self.cmd_a = CurrentCMD_A()
    self.cmd_b = CurrentCMD_B()
    # self.all_javascript = str

  #Ethan's 
  def is_file_or_dir_b(self, input: str):
    if path.isfile(input):
      if regex.search(".js$", input) != None:
        my_js_file = [input]
        return self.validate_javascript_b(my_js_file)

    elif path.isdir(input):
      all_js_files = []
      for subdir, dirs, files in walk(input):
        for f in files:
          a_file = f'{subdir}\\{f}'
          if regex.search(".js$", a_file) != None:
            all_js_files.append(a_file)
      return self.validate_javascript_b(all_js_files)
   
  # https://github.com/klen/pylama
  def validate_javascript_b(self, all_js_files):
    all_js_code = ""
    for a_file in all_js_files:
      with open(a_file) as js_file:
        js = js_file.read()
        all_js_code += f'{js} \n'

    return all_js_code

  #Azez's 
  def is_file_or_dir_a(self, input):
    if path.isfile(input):
      if regex.search(".js$", input) != None:
        my_js_file = [input]
        return self.validate_javascript_a(my_js_file)

    elif path.isdir(input):
      all_js_files = []
      for subdir, dirs, files in walk(input):
        for f in files:
          a_file = f'{subdir}\\{f}'
          if regex.search(".js$", a_file) != None:
            all_js_files.append(a_file)
      return self.validate_javascript_a(all_js_files)

  # https://github.com/klen/pylama
  def validate_javascript_a(self, all_js_files):
    all_js_code = ""
    for a_file in all_js_files:
      with open(a_file) as js_file:
        js = js_file.read()
        all_js_code += f'{js} \n'

    return all_js_code

  #Shared methods 
  def handle_javascript(self, js : str, current_cmd : str):
    "Creates a javascript handler for given set of javascript file(s)"
    my_javascript = JavascriptHandler(js, current_cmd)
    if current_cmd == "a":
      my_javascript.extract_javascript_a()
    else:
      my_javascript.extract_javascript_b()
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
      
      self.cmd_looper(current_cmd, "Converting Code...")

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


    



  
    


    
