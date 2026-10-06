'''23.Print all characters that occur exactly twice.'''

s = input("Enter string: ")
result=""

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count==2:
        if i not in result:
            result+=i+" "
print("Characters that are repeating twice: ",result)