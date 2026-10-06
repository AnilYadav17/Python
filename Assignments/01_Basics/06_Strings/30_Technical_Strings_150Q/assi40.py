'''40.Search all occurrences of a word.'''

s = input("Enter string: ")
ch = input("Enter character: ")

for i in range(len(s)):
    if s[i]==ch:
        print(i,end=" ")
        