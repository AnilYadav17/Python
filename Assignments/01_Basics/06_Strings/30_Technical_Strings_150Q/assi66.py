'''66.Count number of sentences in a paragraph.'''

s = input("Enter Paragraph: ")
count=0

for i in range(len(s)):
    if s[i-1].isalpha()==True and s[i]==".":
        count+=1

print("Count:",count)