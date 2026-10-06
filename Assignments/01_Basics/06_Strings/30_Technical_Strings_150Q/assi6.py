'''6.Convert a string to uppercase.'''

s = input("Enter lowercase string: ")

for i in s:
    print(chr(ord(i)-32),end="")
print()