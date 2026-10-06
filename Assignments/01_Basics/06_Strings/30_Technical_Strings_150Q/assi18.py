'''18.Replace occurrences of a character.'''

s = input("Enter String: ")
ch = input("Target character: ")
ch1 = input("Replacing character: ")
result=""

for i in s:
    if ch==i:
        result+=ch1
    else:
        result+=i
print("Result:",result)