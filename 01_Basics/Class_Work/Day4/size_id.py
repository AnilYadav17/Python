import sys

#1
a = 10
b = 10.5
c = True
d = "String"
e  = None
f = "Anil"
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(f))

#2
x = "A"
print(sys.getsizeof(x))
y = "A"*200
print(sys.getsizeof(y))

#3
x = 10
y = 10
print(id(x))
print(id(y))

#4
x = True
y = True
z = "Anil"
print(id(x),id(y),id(z))   #gives diff ids for z 

#5
x = 10
y = x*100
print(id(x), id(y))     #gives diff ids

#6
a = "Anil"
print(id(a))
a = a+"Yadav"
print(id(a))

#7
a = "Anil"
print(id(a))
a = a
print(id(a))
