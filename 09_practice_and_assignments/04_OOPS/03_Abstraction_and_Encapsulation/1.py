# Assignment 1: Shape Area Calculation
class Shape:
    def calculateArea(self):
        print("Area calculation not defined for Shape.")

class Circle(Shape):
    def calculateArea(self):
        radius = 5
        print(f"Area of circle is: {3.14 * radius * radius}")

class Rectangle(Shape):
    def calculateArea(self):
        length = 10
        width = 5
        print(f"Area of rectangle is: {length * width}")


print(__name__)
if __name__ == "__main__":
    Shape().calculateArea()
    Circle().calculateArea()
    Rectangle().calculateArea()
