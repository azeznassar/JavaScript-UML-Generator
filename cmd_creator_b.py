# pylint: disable="import-error"
from command_line_creator import CommandLineCreator
from current_cmd_b import CurrentCMD_B

class CmdCreatorB(CommandLineCreator):
    
    def create_cmd(self):
        current_cmd = CurrentCMD_B(self.output)
        return current_cmd