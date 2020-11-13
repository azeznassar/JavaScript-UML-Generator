from abc import ABC, abstractmethod

class CommandLineCreator(ABC):
    
    @abstractmethod
    def create_cmd(self):
        pass