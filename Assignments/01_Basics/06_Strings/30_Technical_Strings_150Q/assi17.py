'''17.Remove occurrences of a character.'''

s = input("Enter String: ")
ch = input("Enter index: ")
result=""

for i in s:
    if ch==i:
        pass
    else:
        result+=i
print("Result:",result)