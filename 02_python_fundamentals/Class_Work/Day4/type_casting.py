#implicit type casting 
a  = 20
b  = 20.5
c  = a+b
print("Type of C ", type(c))  

d=a*b
print("Type of D ", type(d))

#EXPLICIT TYPECASTING
#int()
a = int(10.5)
print(a,type(a))
b=int("10")
print(b,type(b))
c = int(float("10.9"))
print(c,type(c))

#float()
a = float("10")
print(a,type(a))
b = float("10.5")
print(b,type(b))
'''c = float(10+5j)
print(c,type(c))   #Gives Error'''

#str()
a = 10
b = 12.56
c = True
d = 3+4j
print(a,str(a),type(str(a)))
print(b,str(b))
print(c,str(c))
print(d,str(d))

a = str(10)
b = str(12.56 )
c = str(True)
d = str(3+4j)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
