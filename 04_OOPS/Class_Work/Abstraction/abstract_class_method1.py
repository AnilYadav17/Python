from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass


obj = Bank()
obj.interest()
