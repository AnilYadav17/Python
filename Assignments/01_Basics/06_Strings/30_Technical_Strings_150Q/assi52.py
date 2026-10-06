'''52. Remove all special characters.'''

s = input("Enter string: ")
result=""

for i in s:
    if i.isalnum()==True or i.isdigit==True or i==" ":
        pass
    else:
        result+=i

print("Result:",result)