'''81.Generate a hash code or UUID.'''
#test -> 3556498


s = input("Enter string:")
hash=0

for i in s:
    hash=(hash*31)+ord(i)
print(hash)
