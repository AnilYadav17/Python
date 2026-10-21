from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def display1(self):
        pass

    @abstractmethod
    def display(self):
        pass

         
class Child(Employee):
    def display(self):
        pass



class Child1(Child):
    def display1(self):
        pass


c = Child1("Anil",100)
