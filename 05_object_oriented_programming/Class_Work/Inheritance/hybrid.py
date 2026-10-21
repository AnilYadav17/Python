class A:
    def show1(self):
        print("A")

class B(A):
    def show2(self):
        print("B")

class C(A):
    def show3(self):
        print("C")

class D(B,C):
    def show4(self):
        print("D")


d1 = D()
d1.show1()
d1.show2()
d1.show3()
d1.show4()
