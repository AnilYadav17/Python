class Person:
    def show(self):
        print("Person Method")
    

class Child(Person):
    def show(self):    
        super().show()     
        print("Child Method")
        
    
c1=Child()
c1.show()

