class Grandparent:
    def fun1(self):
        return "This is from Grand Parent"
    
class Parent(Grandparent):
    def fun2(self):
        return "This is from  Parent"
    
class Child(Parent):
    def fun3(self):
        return "This is from Child"
    
obj = Child()
print(obj.fun1())
print(obj.fun2())
print(obj.fun3())