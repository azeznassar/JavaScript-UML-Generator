
from cmd import Cmd
from abc import ABCMeta, abstractmethod


class CommandLine(Cmd, metaclass=ABCMeta):  # Abstract class
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.user_name = "User"
        self.current_command = ""
        self.user_args = ""

    def emptyline(self):
        pass

    @abstractmethod
    def do_create_uml(self, args):
        pass

    @abstractmethod
    def do_deserialize(self, args):
        pass

    @abstractmethod
    def do_info(self, args):
        pass

    @abstractmethod
    def do_quit(self, args):
        pass

    @abstractmethod
    def do_switch_cmd(self, args):
        pass
