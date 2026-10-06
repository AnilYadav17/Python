'''69.Count how many times 'life' appears in a string.'''

s = input("Enter string: ")
ss = "life"
count=0

for i in range(len(s)-len(ss)+1):
    for j in range(len(ss)):
        if ss[j]!=s[i+j]:
            pass
        else:
            count+=1

print("Count of","life:",int(count/len(ss)))
