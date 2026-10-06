#WAP to create an Abstarct Class Payment with pay as a Abstract Method , 
#Now create different payment classess (New)

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def __init__(self,a):
            self.a = a

    def pay(self):
        print("UPI Payment",self.a)


class Netbanking(Payment):
    def __init__(self,a):
                self.a = a
    
    def pay(self):
            print("Netbanking Payment",self.a)


u1 = UPI(10)
u1.pay()

N1 = Netbanking(20)
N1.pay()