'''57.Merge two strings alternatively.'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result=""
k=0

for i in s1:
    result+=i
    result+=s2[k]
    k+=1

print(result)