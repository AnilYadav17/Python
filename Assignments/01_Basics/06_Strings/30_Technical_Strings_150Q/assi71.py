'''71.Print all substrings.'''

s = input("Enter string: ")
result=""

for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]
        result+=sub+","

print(f"Count: {result}")