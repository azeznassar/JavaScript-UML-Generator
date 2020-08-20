from cmd import Cmd
from abc import ABCMeta, abstractmethod

class CommandLine(Cmd, metaclass=ABCMeta):  # Abstract class
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "User"

    @abstractmethod
    def display_output(self):
        pass

    @abstractmethod
    def do_help(self):
        pass

    @abstractmethod
    def do_create_uml(self):
        pass

    @abstractmethod
    def do_deserialize(self):
        pass

    @abstractmethod
    def do_load(self):
        pass

    @abstractmethod
    def do_info(self):
        pass

    @abstractmethod
    def do_quit(self):
        pass

    @abstractmethod
    def do_switch_cmd(self):
        pass
