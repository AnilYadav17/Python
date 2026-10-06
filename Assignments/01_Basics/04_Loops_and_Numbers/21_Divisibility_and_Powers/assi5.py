'''Analyse and Print as per pattern
A
AB
ABC
ABCD
ABCDE'''

num = int(input("Enter Number = "))
i = 1

while i<=num:
    ch=65
    print()
    j=1
    while j<=i:
        print(chr(ch),end="")
        ch+=1
        j+=1
    i+=1