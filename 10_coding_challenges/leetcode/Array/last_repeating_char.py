# S = "programing" 
S = "mississippi"
repeated=[]
seen=[]
for i in S:
    if i not in seen:
        if S.count(i)>1:
            repeated.append(i)
        seen.append(i)

print(repeated[-1])