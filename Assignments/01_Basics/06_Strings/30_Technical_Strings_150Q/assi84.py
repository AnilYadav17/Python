'''84.Print ASCII value of each character.'''

n = input("Enter characters (separate by ,): ")
l = n.split(",")
result=""

for i in l:
    result+=str(ord(i))+","
print(result)