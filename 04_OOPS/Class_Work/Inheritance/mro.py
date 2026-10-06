class Father:
    def show(self):
        print("Father Show Method")

class Mother:
    def show(self):
        print("Mother Show Method")

class Child(Father,Mother):
    def show(self):
        super().show()
        print("Child Show")

c = Child()
c.show()
