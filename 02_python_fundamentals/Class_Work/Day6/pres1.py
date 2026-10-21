a = 256 
b = 256

print(id(a))
print(id(b))
print(a is b)


x = 257
y = 257
print(id(x) is id(y))


a = int("256")
b = int("256")
print(id(a) is id(b))
x = int("257")
y = int("257")
print(id(x) is id(y))


a = "bahu"+"3"
print(a)
#b = "Anil "*"3"
#b = "Anil"*3.0
#b = 10%0 can not divisible by zero

print(b)


