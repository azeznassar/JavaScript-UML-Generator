#Azez's CMD

# pylint: disable="import-error"
from command_line import CommandLine

class CurrentCMD_A(CommandLine):

    def __init__(self):
        CommandLine.__init__(self)

    #For testing purposes
    # def do_greet(self, the_name):
    #     """
    #     Usage: greet [the_name]
    #     Greet the named person
    #     :parameter the_name: a string representing a person's name
    #     :return: None
    #     """
    #     if the_name:
    #         print("Hello " + the_name)
    #     else:
    #         print("Hello " + self.my_name)    

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
        pass


    def do_load(self, args):
        pass

    def do_info(self, args): 
        """
        Usage: info
        Displays info about the software and how to use the commands
        """
        print("""
            JS2UML: Generate UML 2 Class Diagrams from JavaScript file(s)

             The software has the following options/commands:
             * help
             * create_uml
             * deserialize
             * load
             * info
             * quit
             * switch_cmd

             The software was developed by Azez Nassar & Ethan Bray in Python3
             Version: 0.0.1

             Source: https://github.com/AzezNassar
             """)
    
        #Testing purposes
        if args:
            print(f"!!!!!!!{args}!!!!!!!")
        else:
            print('no arg given')
            print(f"!!!!!!!{args}!!!!!!!")


    def do_switch_cmd(self, args):
        print("Swapping to Ethan's Command Line")
        self.current_command = "do_switch_cmd"
        return True

    def do_quit(self, args):
        print("Thank you for using JS2UML")
        return True
