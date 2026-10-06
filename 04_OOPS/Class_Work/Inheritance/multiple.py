class Father:
    def house(self):
        print("Father has a house")

    def laptop(self):
        print("Father has a laptop")

class Mother:
    def laptop(self):
        print("Mother has a laptop")


# class Child(Father,Mother):
#     def nothig(self):
#         print("Child has Nothing")


class Child(Mother,Father):      #Here Python use MRO , if 
    def nothig(self):
        print("Child has Nothing")

 
c1 = Child()
c1.house()
c1.laptop()
c1.nothig()