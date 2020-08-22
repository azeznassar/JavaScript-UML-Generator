#Ethan's CMD

# pylint: disable="import-error"
from command_line import CommandLine

class CurrentCMD_B(CommandLine):

    def __init__(self):
        CommandLine.__init__(self)

    def do_create_uml(self, args):
        pass

    def do_deserialize(self, args):
        pass

    def do_load(self, args):
        self.my_input_handler.validate_javascript(args)

    def do_info(self, args):
        return

    def do_quit(self, args):
        print("Leaving System")
        return True

    def do_switch_cmd(self, args):
        print("Swapping to Azez's Command Line")
        return 0

    def default(self, line):
        pass

    