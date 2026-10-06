'''12.
a
ab
abc
abcd
abcde'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(ord("a")+j-1),end="")
    print()