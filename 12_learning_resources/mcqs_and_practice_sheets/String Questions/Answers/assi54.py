'''54.Replace duplicate chars with '$'.'''

s = input("Enter string: ")
result=""

for i in s:
    if i in result:
        result+="$"
    else:
        result+=i

print("Result:",result)