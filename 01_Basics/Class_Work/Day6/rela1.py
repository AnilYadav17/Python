#relational operators

a = 5
b = 2
print(a==b) #FALSE
print(a<b)  #FALSE
print(a>b)  #TRUE
print(a!=b) #TRUE
c = 5
print(a>c) #FALSE
print(a<=c) #TRUE
print(a!=c) #FALSE

print(5==5.0) #TRUE

a = "Anil"
b = "Yadav"
print(a>b) #false because of first character compairision (unicode of A is smaller than Y)
print("anil" == "anil") #true

a = "deeA"
b = "deeB"
print(a<b) #true

print(5 == "5") #false
print("True">"False")
#print("True">True) #error 

print(True==True)
print(True>False)
print(True!=False)

print(0==True)
print(""==False)
print([]==False)
