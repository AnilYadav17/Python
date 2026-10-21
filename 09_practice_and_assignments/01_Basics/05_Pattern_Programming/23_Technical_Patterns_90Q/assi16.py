'''16.
a
bc
def
ghij
klmno'''

c = ord("a")
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(c),end="")
        c+=1
    print()