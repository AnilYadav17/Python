'''11.
A
AB
ABC
ABCD
ABCDE'''

#Ascii of A is 65
#print(ord("A")) 

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(ord("A")+j-1),end="")
    print()