'''10.Trim leading, trailing, or extra spaces.'''

s = input("Enter String: ")
l = s.split()
result=""

for i in l:
    if i!=" ":
        result+=i+" "

print(result)