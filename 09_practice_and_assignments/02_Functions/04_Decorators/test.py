s = "Anil adav"

s = s.split()
s1 = ("aeiouAEIOU") 
c=0
for i in s:
    if i[0] in s1:
        c+=1

print(c)