'''58.Rotate characters left by 2 positions.'''

s = input("Input string: ")
result=""

for i in range(2,len(s)):
    result+=s[i]

result+=s[:2]
print("Result:",result)