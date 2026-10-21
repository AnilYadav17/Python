from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculatebonus(self):
        pass

    def display(self):
         print("Employee Name:",self.name)
         print("Salary:",self.salary)

class Manager(Employee):
    def calculatebonus(self):
          bonus = self.salary*0.2
          print("Manager Bonus:",bonus)


class Developer(Employee):
    def calculatebonus(self):
          bonus = self.salary*0.1
          print("Developer Bonus:",bonus)


obj1 = Manager("abc",10000)
obj1.calculatebonus()
obj1.display()

obj2 = Developer("xyz",200000)    #-> If no argument were given then it will rise an error("TypeError: Employee.__init__() missing 2 required positional arguments: 'name' and 'salary'")
obj2.calculatebonus()
obj2.display()
