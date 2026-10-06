class Emp:
    def __init__(self,id,name,salary):
        self.__name = name
        self.__id = id 
        self.__salary = salary

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary    
    
    def set_id(self,id):
        self.__id = id

    def set_salary(self,salary):
        if salary>1000:
            self.__salary = salary
        else:
            print("Invalid Salary!")

    def set_name(self,name):
        if name.strip()!="":
            self.__name=name
        else:
            print("Invalid name!")

e1 = Emp(101,"Anil",100000)
print(e1.get_id())
print(e1.get_name())
print(e1.get_salary())

e1.set_name("Anil")
print(e1.get_name())
e1.set_salary(1000000)
print(e1.get_salary())