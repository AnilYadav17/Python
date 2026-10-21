n = int(input("Enter the number of students: "))
d=dict()

for i in range(n):
    key = input("Enter name: ")
    value = input("Enter marks%: ")
    d[key]=value

print(list(d.items()))
print(list(d.values()))
print(list(d.keys()))