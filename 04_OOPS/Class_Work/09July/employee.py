class Employee:
    def __init__(self,salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

e1 = Employee(10000)
print(e1.salary)
e1.salary = 5000
print(e1.salary)