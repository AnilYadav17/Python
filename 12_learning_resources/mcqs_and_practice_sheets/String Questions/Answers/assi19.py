'''19.Find the highest frequency character.'''

s = input("Enter String: ")
result=""
max=0

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if max<count:
        max=count
        result=i

print(f"{result} is highest frequency character, {max} times")