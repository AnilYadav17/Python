'''20.Find the lowest frequency character.'''

s = input("Enter String: ")
result=""
low=100
max=0

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if low>count:
        low=count
        result=i+","
    if low==count and i not in result:
        result+=i+","
        max=count

print(f"{result} are lowest frequency character, {max} times")