'''38.Reverse words without split().'''

s = input("Enter string: ")
word=""

for i in range(len(s)):
    if s[i]!=" ":
        word=s[i]+word
    else:
        print(word,end=" ")
        word=""

print(word)
