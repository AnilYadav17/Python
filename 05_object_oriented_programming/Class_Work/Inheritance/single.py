class Parent:
    def fun1(self):
        return "Parent Function1"
    
class Child(Parent):
    def fun2(self):
        return "Child FUnction2"
    
obj = Child()
print(obj.fun1())
print(obj.fun2())