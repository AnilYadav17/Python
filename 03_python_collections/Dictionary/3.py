n = int(input("Enter number of items: "))

d={}
for i in range(n):
   key=input("Enter Key: ") 
   value=int(input("Enter value: "))
   d[key]=value

print(type(d),d)
print("Sum:",sum(d.values()))