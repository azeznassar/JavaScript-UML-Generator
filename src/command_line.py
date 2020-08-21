from cmd import Cmd
from abc import ABCMeta, abstractmethod

class CommandLine(Cmd, metaclass=ABCMeta):  # Abstract class
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "User"

    def emptyline(self):
        pass

    @abstractmethod
    def do_create_uml(self, args):
        pass

    @abstractmethod
    def do_deserialize(self, args):
        pass

    @abstractmethod
    def do_load(self, args):
        pass

    @abstractmethod
    def do_info(self, args):
        pass

    @abstractmethod
    def do_switch_cmd(self, args):
        pass
