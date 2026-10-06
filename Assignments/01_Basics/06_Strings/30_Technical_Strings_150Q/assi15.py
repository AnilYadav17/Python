'''15.Find the last occurrence of a character.'''

s = input("Enter String: ")
ch = input("Enter index: ")

for i in range(len(s)-1, -1, -1):
    if s[i]==ch:
        print(i)
        break
    