'''67.Count how many times a substring appears.'''

s = input("Enter string: ")
ss = input("Enter substring: ")
count=0

for i in range(len(s)-len(ss)+1):
    for j in range(len(ss)):
        if ss[j]!=s[i+j]:
            pass
        else:
            count+=1

print("Count of SubString:",int(count/len(ss)))
