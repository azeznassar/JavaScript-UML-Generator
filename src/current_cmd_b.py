#Ethan's CMD

# pylint: disable="import-error"
from command_line import CommandLine

class CurrentCMD_B(CommandLine):

    def __init__(self):
        CommandLine.__init__(self)

    def do_create_uml(self, args):
        self.current_command = "do_create_uml"
        self.user_args = args
        return True

    def do_deserialize(self, args):
        pass

    def do_load(self, args):
        self.current_command = "do_load"
        return True

    def do_info(self, args):
        print ("Ethans info")

    def do_quit(self, args):
        print("Leaving System")
        self.current_command = "do_quit"
        return True

    def do_switch_cmd(self, args):
        print("Swapping to Azez's Command Line")
        self.current_command = "do_switch_cmd"
        return True

    def default(self, line):
        pass

    