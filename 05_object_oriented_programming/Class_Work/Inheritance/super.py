class Person:
    def __init__(self):
        print("Person Constructor")
    
class Employee(Person):
    def __init__(self):         #Without this only child class is called.
        super().__init__()
        print("Employee Constructor")
    
emp=Employee()


