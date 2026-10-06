'''41. Check if a string contains a substring (without using built-in method). '''

s = input("Enter string: ")
ch = input("Enter character: ")
found =False

for i in range(len(s)-len(ch)+1):
    match=True
    for j in range(len(ch)):
        if ch[j]!=s[i+j]:
            match=False
            break
        
    if match==True:
        found=True
        break

if found:
    print(True)
else:
    print(False)
            
