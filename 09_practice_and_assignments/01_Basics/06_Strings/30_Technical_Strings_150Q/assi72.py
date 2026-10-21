'''72.Print all substrings of length n.'''
#Input:S = "abc", n = 2    ,Output:"ab, bc"

s = input("Enter string: ")
result=""

for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]
        if len(sub)==2:
            result+=sub+","

print(f"Count: {result}")