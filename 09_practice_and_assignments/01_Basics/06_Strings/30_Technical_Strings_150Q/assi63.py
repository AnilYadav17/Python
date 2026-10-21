'''63.Count frequency of each character.'''

s = input("Enter string: ")
result=""

for i in s:
    if i not in result:
        count=0
        for j in s:
            if i==j:
                count+=1
        
        print(f"{i}:{count}",end=", ")
        result+=i