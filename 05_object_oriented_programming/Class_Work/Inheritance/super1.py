class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    
class Employee(Person):
    def __init__(self,name,age,address,salary):         
        super().__init__(name,age,address)
        self.salary = salary
        
    
emp=Employee("Anil",22,"Dewas",9999999)
print(emp.name,emp.age,emp.address,emp.salary)


