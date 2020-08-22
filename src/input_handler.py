# Input Handler
import re as regex

class InputHandler():
  """Handles User Commands that require action beyond basic cmd output"""

  #Ethan's 
  def is_file_or_dir_b(self, path: str) -> bool:
    "Returns true if the path ends with .js and the end .js is not at the start as well"
    if regex.search(".js$", path) != None and regex.search(".js$", path).span() != (0, 3):
      return True # Is a File
    else:
      return False # Is a Folder

  def validate_javascript_b(self, path: str):
    "Formats and loads the selected javascript file(s)"

    if self.is_file_or_dir_b(path):
      print(f'Loading the single file {path}')
    
    else:
      print(f'Loading all files {path}')

  #Azez's 
  def is_file_or_dir_a(self, input):
    if regex.search(".js$", input) != None:
      return f"Your JS file {input} is being processed"
    else:
      return f"Your directory {input} is being processed"

  def validate_javascript_a(self, input):
    #standardjs python package?
    pass

  #Shared methods 
  def handle_javascript(self):
    "Creates a javascript handler for given set of javascript file(s)"




  
    


    
