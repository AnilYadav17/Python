'''56. Reverse only consonents.'''
#input: hello , output:lelho

s = input("Enter string: ")
vowels="aeiouAEIOU"
result=""
rev=""

for i in s:
    if i not in vowels:
        rev=i+rev

k=0
for i in s:
    if i  in vowels:
        result+=i
    else:
        result+=rev[k]
        k+=1

print(result)

