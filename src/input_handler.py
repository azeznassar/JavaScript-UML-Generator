# Input Handler Stuff Ethan
from esprima import tokenize, parseScript
from plantuml import PlantUML
from current_cmd_a import CurrentCMD_A
from current_cmd_b import CurrentCMD_B
import ast
import re as regex

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""

  def __init__(self):
    self.cmd_a = CurrentCMD_A()
    self.cmd_b = CurrentCMD_B()

  def is_file_or_dir(self, path: str) -> bool:
    "Returns true if the path ends with .js and the end .js is not at the start as well"
    if regex.search(".js$", path) != None and regex.search(".js$", path).span() != (0, 3):
      return True # Is a File
    else:
      return False # Is a Folder

  def validate_javascript(self, path: str):
    "Formats and loads the selected javascript file(s)"

    if self.is_file_or_dir(path):
      print(f'Loading the single file {path}')
    
    else:
      print(f'Loading all files {path}')

  def handle_javascript(self):
    "Creates a javascript handler for given set of javascript file(s)"


if __name__ == "__main__":
  import sys
  input_handler = InputHandler()
  system_runner = input_handler.cmd_a # Default CMD is Azez's
  # print(sys.argv[0]) # src\input_handler.py 0 or 1
  if len(sys.argv) > 1:
    if sys.argv[1] == "0":
      system_runner = input_handler.cmd_a # Azez CMD
    if sys.argv[1] == "1":
      system_runner = input_handler.cmd_b # Ethan CMD
  
  system_runner.cmdloop()


  
    


    
