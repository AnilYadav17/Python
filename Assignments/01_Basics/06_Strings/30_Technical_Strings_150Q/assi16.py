'''16. Count total occurrences of a character.'''

s = input("Enter String: ")
ch = input("Enter index: ")
count=0

for i in range(len(s)-1, -1, -1):
    if s[i]==ch:
        count+=1
    
print(f"Total occurrences of {ch} is {count}")