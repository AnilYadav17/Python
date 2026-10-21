class Book:
    def __init__(self,no,name,writer):
        self.__no = no
        self.__name = name
        self.__writer = writer


    @property
    def no(self):
        return self.__no
    
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
    def writer(self):
        return self.__writer
    @writer.setter
    def writer(self,writer):
        self.__writer = writer
    @writer.deleter
    def writer(self):
        del self.__writer
b1 = Book(101,"The Great Day","Anil")
print(b1.no,b1.name,b1.writer)
b1.name="The amazing Great Day"
print(b1.no,b1.name,b1.writer)


del b1.name    #_. 
#print(b1.no,b1.name,b1.writer)
