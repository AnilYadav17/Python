'''51. Extract only digits.'''

s = input("Enter string: ")
result=""

for i in s:
    if i>="0" and i<="9":
        result+=i

print("Result:",result)