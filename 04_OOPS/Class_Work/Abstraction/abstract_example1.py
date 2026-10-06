from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r


class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return 0.5*self.l*self.b

    
obj1 = Circle(int(input("Enter Circle Radius: ")))
print(obj1.area())

obj2 = Rectangle(int(input("Enter Length: ")),int(input("Enter Bridth: ")))
print(obj2.area())