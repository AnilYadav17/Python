class A:
    def show1(self):
        print("A")

class B(A):
    def show2(self):
        print("B")

class C(A):
    def show3(self):
        print("C")


c = C()
c.show1()
c.show3()

#Can not access Sibling classes
