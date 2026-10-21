n = int(input("Enter the number of students: "))
d=dict()

for i in range(n):
    key = input("Enter name: ")
    value = input("Enter marks%: ")
    d[key]=value

#Adding Elements
k1 = input("\nEnter student name to Update: ")
s1 = input("Enter %marks name to update: ")
if k1 in d:
    print("\nKey already found, so Updating the previous value: ")
    d[k1]=s1
else:
    print("\nKey not found, so Adding the value: ")
    d[k1]=s1
print("\nAll Students with Marks: ")
print("Name\t\t%Marks")
for i in d:
    print(i,"\t\t",d[i])