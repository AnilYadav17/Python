'''88. Rearrange a string so that identical characters are at least d distance apart.'''
#aaabc  ,2 ->  abaca

#incomplete , added to remain
s = input("Enter string: ")
d = int(input("Enter distance: "))
result=""

for i in range(len(s)//d):
    result+=s[::d+1]
    s = s[len(s)//d:]
    print(s)

print(result)