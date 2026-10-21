'''53.Remove punctuation.'''

s = input("Enter string: ")
result=""

for i in s:
    if i.isalnum()==True or i.isdigit==True or i==" ":
        result+=i

print("Result:",result)