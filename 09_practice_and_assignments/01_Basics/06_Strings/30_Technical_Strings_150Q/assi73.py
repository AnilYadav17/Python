'''73.Find the longest palindromic substring.'''
#babad -> bab
s = input("Enter string: ")
result=""
max=0

for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]
        if len(sub)>=max and sub==sub[::-1]:
            max=len(sub)
            result=sub

print(f"Count: {result}")