'''86.Print all permutations of a string without repetition.'''
#xy -> xy,yx

s = input("Enter string: ")
used=[]
result=""

for i in s:
    for j in s:
        if i!=j:
            result+=i+j+" "

    if result not in used:
        used.append(result)
print(result)
