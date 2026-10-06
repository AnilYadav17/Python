'''43.Check if two strings are rotations of each other.'''

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
flag=0

if len(s1)!=len(s2):
    flag=0
else:
    for i in range(len(s1)):
        if s1[i]==s2[len(s1)-i-1]:
            flag=1
        else:
            flag=0

if flag==1:
    print("Both strings are rotations of each other")
else:
    print("Both strings are not rotations of each other")