a = 10
print(a)
#10 = 20 can not assign literal errror
a += 5
print(a)
a -= 5
print(a)
a *=5
print(a)
a /=5
print(a)


a = b = 10
print(a,b)

#a+=b+=2 can not chain short hand op
a=5
b=2
a +=b*3 
print("\n",a,b)

a = 17
a//=3+1
print("a//4 : ",a)
