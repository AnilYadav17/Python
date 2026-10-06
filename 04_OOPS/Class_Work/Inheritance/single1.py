class Person:
    def __init__(self,name):
        self.name=name
    
class Employee(Person):
    def showrole(self):
        return f"{self.name} is a employee"


e1 = Employee("Anil")
print(e1.showrole())
