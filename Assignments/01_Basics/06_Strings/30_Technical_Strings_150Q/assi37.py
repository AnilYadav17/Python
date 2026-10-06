'''37.Reverse each word.'''

s = input("Enter string: ")
l = s.split()
result=""

for i in l:
    for j in range(len(i)-1,-1,-1):
        result+=i[j]
    result+=" "
print(result)