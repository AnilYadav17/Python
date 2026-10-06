class Product:
    def __init__(self,id,name,price):
        self.__id = id
        self.__name = name
        self.__price = price

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @name.deleter
    def name(self):
        del self.__name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price
    @price.deleter
    def price(self):
        del self.__price

    
p1 = Product(101,"Laptop",10000)
print(p1.id,p1.name,p1.price)

#p1.id = 102  ->> We did not created any setter attribute for id
p1.name = "Gaming Laptop"
p1.price = 2345677654
print(p1.id,p1.name,p1.price)

#del p1.price
#print(p1.price)