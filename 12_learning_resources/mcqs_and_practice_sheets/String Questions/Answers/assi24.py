'''24.Check if all characters in a string are unique.'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
flag=1
for i in s1:
    count=0
    for j in s1:
        if i==j:
            count+=1
    if count>1:
        flag=0
        break
if flag==1:
    print("True")
else:
    print("False")

flag=1
for i in s2:
    count=0
    for j in s2:
        if i==j:
            count+=1
    if count>1:
        flag=0
        break
if flag==1:
    print("True")
else:
    print("False")
