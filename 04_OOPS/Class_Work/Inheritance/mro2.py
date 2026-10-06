class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A,B):
    def show(self):
        A.show(self)
        B.show(self)
        print("C")


c = C()
c.show()