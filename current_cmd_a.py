
# Azez's CMD

# pylint: disable="import-error"
from command_line import CommandLine
from serializer import Serializer


class CurrentCMD_A(CommandLine):

    def __init__(self):
        CommandLine.__init__(self)

    def do_create_uml(self, args):
        """
        Usage: create_uml [-help] [-save] input output
        Greet the named person
        :optional parameter -save: Saves JS data to SQL lite DB
        :parameter input: Input file/directory for JS
        :parameter output: Output directory for generated image
        """
        self.current_command = "do_create_uml"
        self.user_args = args
        return True

    def help_create_uml(self):
        """
        Usage: ? create_uml OR help create_uml
        Displays info about the create_uml command
        """
        print('Generate UML 2 Class Diagrams from JavaScript file(s)')

    def do_deserialize(self, args):
        self.current_command = "do_deserialize"
        self.user_args = args
        return True

    def do_info(self, args):
        """
        Usage: info
        Displays information about the software,
        such as version number and authors.
        """
        print("""
            JS2UML: Generate UML 2 Class Diagrams from JavaScript file(s)

            The software was developed by Azez Nassar & Ethan Bray in Python3
            Version: 1.0

            Source: https://github.com/azeznassar/JavaScript-UML-Generator
             """)

    def do_help(self, args):
        print("""
                ================================================
                create_uml deserialize info switch_cmd help exit


                create_uml:
                    usage: create_uml js_input
                    Generate an image of an UML class diagram
                    from inputted JavaScript source code file(s)

                positional arguments:
                    js_input	input JavaScript file / dirs


                deserialize:
                    usage: deserialize [-d]
                    Display the deserialized JavaScript class 
                    information that is serialized from the create_uml command

                optional arguments:
                    -d		Deletes the serialized data file 
                            after deserializing and display it


                info:
                    usage: info
                    Displays information about the software, 
                    such as version number and authors.


                switch_cmd:
                    usage: switch_cmd
                    Switchs from the current cmd implementation
                    to the other available implementation. 
                    (all commands are the same)


                help:
                    usage: help
                    Displays help information about each available 
                    command, such as, usage and possible arguments


                quit:
                    usage: quit
                    Exits from the program
        """)

    def do_switch_cmd(self, args):
        print("Swapping to Ethan's Command Line")
        self.current_command = "do_switch_cmd"
        return True

    def do_quit(self, args):
        print("Thank you for using JS2UML")
        self.current_command = "do_quit"
        return True
