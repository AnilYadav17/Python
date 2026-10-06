class  Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name,"\nAge:",self.age)

s1 = Student("Anil",101)
s1.display()