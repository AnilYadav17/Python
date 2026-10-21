n = int(input("Enter the number of students: "))
d=dict()

for i in range(n):
    key = input("Enter name: ")
    value = input("Enter marks%: ")
    d[key]=value

print("\nName\t\tMarks(%)")
for i in d:
    print(i,"\t\t",d[i])

