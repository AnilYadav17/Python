#Please  ensure Module1 ,Module2 ,MOdule3 exist in same directory

#from module1 import add
#import module1 as m1
from  module1 import func,add
from module3 import func    #here module3 will win 
print(add(1,2))
print(func())

