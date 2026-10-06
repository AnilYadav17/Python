'''8.Toggle the case of each character.'''

s = input("Enter string: ")

for i in s:
    if i>="A" and i<="Z":
        print(chr(ord(i)+32),end="")
    else:
        print(chr(ord(i)-32),end="")
print()