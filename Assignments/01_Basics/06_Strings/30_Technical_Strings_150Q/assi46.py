'''46.Check if a substring appears at both the start and end.'''

s = input("Enter string: ")
ss = input("Enter substring: ")
prefix_match=True
suffix_match=True

for i in range(len(ss)):
    if s[i]!=ss[i]:
        prefix_match=False
        break

if s[-len(ss):] != ss:
        suffix_match=False

print(prefix_match and suffix_match)