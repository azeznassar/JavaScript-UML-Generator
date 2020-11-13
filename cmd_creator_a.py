# pylint: disable="import-error"
from command_line_creator import CommandLineCreator
from current_cmd_a import CurrentCMD_A

class CmdCreatorA(CommandLineCreator):

    def create_cmd(self):
        current_cmd = CurrentCMD_A(self.output)
        return current_cmd