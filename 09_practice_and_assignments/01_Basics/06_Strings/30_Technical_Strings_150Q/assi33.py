'''33. Find the longest word.'''

s = input("Enter string: ")
l = s.split()
max=0
result=""

for i in l:
    if max<len(i):
        max=len(i)
        result=i

print(f"{result} is largest word with length {max}")