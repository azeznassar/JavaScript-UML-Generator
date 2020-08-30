
#Ethan's CMD

# pylint: disable="import-error"
from command_line import CommandLine
from serializer import Serializer

class CurrentCMD_B(CommandLine):

    def __init__(self):
        CommandLine.__init__(self)

    def do_create_uml(self, args):
        self.current_command = "do_create_uml"
        self.user_args = args
        return True

    def do_deserialize(self, args):
        self.current_command = "do_deserialize"
        self.user_args = args
        return True

    def do_info(self, args):
        print("""
            JS2UML: Generate UML 2 Class Diagrams from JavaScript file(s)

            The software was developed by Azez Nassar & Ethan Bray in Python3
            Version: 1.0

            Source: https://github.com/azeznassar/JavaScript-UML-Generator
             """)

    def do_quit(self, args):
        print("Leaving System")
        self.current_command = "do_quit"
        return True

    def do_switch_cmd(self, args):
        print("Swapping to Azez's Command Line")
        self.current_command = "do_switch_cmd"
        return True

    def do_help(self, args):
        my_help_string = """
            ========================================
            create_uml   deserialize   info   help   switch_cmd   quit

            create_uml:
                usage: create_uml file_or_path
                description: Creates a UML diagram from the specified javascript file or directory(s)

            deserialize:
                usage: deserialize [-d]
                optional arguments: [-d] - Deletes the serialized file(s) after printing data
                description: Prints deserialized class data stored in serialized format
            
            info:
                usage: info
                description: displays program info, current cmd author, version.

            help:
                usage: help
                description: displays this messsage explaining commands

            switch_cmd:
                usage: switch_cmd
                description: switches the cmd to the other authors cmd

            quit:
                usage: quit
                description: quits the cmd back to the terminal session
            ========================================  
        """
        print(my_help_string)

    def default(self, line):
        print (f"Sorry, the command: '{line}' was not recognized, type 'help' to learn about all commands")

    