'''75.Find the longest common prefix among strings.'''
#Strings = ["flower", "flow", "flight"]   ->    output: fl

s = input("Enter string: ")
l = s.split()
result=""

for i in range(len(l)):
    for j in range(len(l[i])):
        if  l[i][j] == l[i+1][j] == l[i+2][j]:
            result+=l[i][j]
        else:
            break

print(result)