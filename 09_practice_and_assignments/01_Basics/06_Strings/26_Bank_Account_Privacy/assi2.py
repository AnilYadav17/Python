'''2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST'''

name = input("Enter employee name: ")
result=""

for i in range(len(name)):
    if ord(name[i])>ord("Z"):
        if i==0 or name[i-1]==" ":
            upper=ord(name[i])-32
            result=result+chr(upper)
    else:
        if i==0 or name[i-1]==" ":
            result=result+name[i]
print(result)