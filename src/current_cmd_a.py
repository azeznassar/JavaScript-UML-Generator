#Azez's CMD

from command_line import CommandLine

class CurrentCMD_A(CommandLine):
    def display_output(self):
        print("test")

    #For testing purposes
    def do_greet(self, the_name):
        """
        Syntax: greet [the_name]
        Greet the named person
        :param the_name: a string representing a person's name
        :return: None
        """
        if the_name:
            print("Hello " + the_name)
        else:
            print("Hello " + self.my_name)

    def do_help(self):
        pass

    def do_create_uml(self):
        pass

    def do_deserialize(self):
        pass

    def do_load(self):
        pass

    def do_info(self):
        pass

    def do_quit(self):
        pass

    def do_switch_cmd(self):
        pass