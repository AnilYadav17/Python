'''42.Check if two strings are equal without equals().'''

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
flag=0

if len(s1)!=len(s2):
    flag=0
else:
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            flag=1
        else:
            flag=0

if flag==1:
    print("Both strings are equal")
else:
    print("Both strings are not equal")