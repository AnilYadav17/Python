'''50.Remove all digits.'''

s = input("Enter string: ")
result=""

for i in s:
    if i>="0" and i<="9":
        pass
    else:
        result+=i

print("Result:",result)