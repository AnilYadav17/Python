'''36.Reverse order of words.'''

s = input("Enter string: ")
l = s.split()
result=""

for i in range(len(l)-1,-1,-1):
    result+=l[i]+" "

print(result)