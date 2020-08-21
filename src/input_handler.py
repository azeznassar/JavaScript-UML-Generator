# Input Handler Stuff Ethan
import re

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""

  def is_file_or_dir(self, path: str) -> bool:
    "Returns true if the path ends with .js and the end .js is not at the start as well"
    if re.search(".js$", path) != None and re.search(".js$", path).span() != (0, 3):
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




  
    


    
