'''14.Find the first occurrence of a character.'''

s = input("Enter String: ")
ch = input("Enter index: ")

for i in range(len(s)):
    if s[i]==ch:
        print(i)
        break
    