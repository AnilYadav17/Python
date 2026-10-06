'''28.Count occurrences of a word.'''

s = input("Enter string (to count): ")
ch = input("Enter word: ")
l = s.split()
count=0

for i in l:
    if ch==i:
        count+=1

print(f"{ch} found {count} times")