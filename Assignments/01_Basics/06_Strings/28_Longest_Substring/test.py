s  =  input("Enter String: ")
ch = input("Enter Target:")

o = ""

for i in s:
    count=0
    if ch == i:
        count+=1
    if count==1:
        o+=i
        break
    else:
        o+=i

print("Output ",o)