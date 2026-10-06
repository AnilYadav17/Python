'''7.Convert a string to lowercase.'''

s = input("Enter uppercase string: ")

for i in s:
    print(chr(ord(i)+32),end="")
print()