'''29. Remove occurrences of a word.'''

s = input("Enter string (to remove): ")
ch = input("Enter word: ")
l = s.split()
result=""
count=0

for i in l:
    if ch==i:
        pass
    else:
        result+=i

print("Updated string: ",result)