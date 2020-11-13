from abc import ABC, abstractmethod

class CommandLineCreator(ABC):
    def __init__(self, output):
        self.output = output
        
    @abstractmethod
    def create_cmd(self):
        pass