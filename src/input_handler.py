
# Input Handler
from esprima import tokenize, parseScript
from plantuml import PlantUML
# pylint: disable="import-error"
from current_cmd_a import CurrentCMD_A
from current_cmd_b import CurrentCMD_B

from javascript_handler import JavascriptHandler

#import ast
import re as regex

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""
  
  def __init__(self):
    self.cmd_a = CurrentCMD_A()
    self.cmd_b = CurrentCMD_B()
    # self.all_javascript = str

  #Ethan's 
  def is_file_or_dir_b(self, path: str) -> bool:
    "Returns true if the path ends with .js and the end .js is not at the start as well"
    if regex.search(".js$", path) != None and regex.search(".js$", path).span() != (0, 3):
      return True # Is a File
    else:
      return False # Is a Folder

  # https://github.com/klen/pylama
  def validate_javascript_b(self, input):
    f = open(input, 'r')
    js_file = f.read()
    f.close()
    return js_file

  #Azez's 
  def is_file_or_dir_a(self, input):
    my_data = self.validate_javascript_a(input)
    if regex.search(".js$", input) != None:
      my_data = self.validate_javascript_a(input)
      return f"Your JS file {input} is being processed it gave: {my_data}"
    else:
      return f"Your directory {input} is being processed it gave: {my_data}"

  # https://github.com/klen/pylama
  def validate_javascript_a(self, input):
    f = open(input, 'r')
    js_file = f.read()
    f.close()
    return js_file

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
        my_data = self.validate_javascript_b(current_cmd.user_args)
        self.handle_javascript(my_data, "b")
      else:
        my_data = self.validate_javascript_a(current_cmd.user_args)
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


    



  
    


    
