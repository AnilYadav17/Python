'''25.Count total words in a string.'''

s = input("Enter String: ")
# l = s.split()
# count=0

# for i in l:
#         count+=1

# print(count)

count=0

for i in range(len(s)):
    if s[i]!=" ":
        if i==0 or s[i-1]==" ":
               count+=1

print(count)