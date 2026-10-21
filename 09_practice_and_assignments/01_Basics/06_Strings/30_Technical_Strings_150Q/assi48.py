'''48.Remove all vowels.'''

s = input("Enter string: ")
result=""
vowels = "aeiouAEIOU"


for i in s:
    if i not in vowels:
        result += i

print("Result:",result)