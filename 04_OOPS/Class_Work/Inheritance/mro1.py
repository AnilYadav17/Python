class Person:
    def __init__(self,name):
        self.name = name
        print("Person contructor")

class Employee:
    def __init__(self,name,salary):
        Person.__init__(self,name)
        self.salary = salary
        print("Employee Constructor")

obj =  Employee("Anil",10000)