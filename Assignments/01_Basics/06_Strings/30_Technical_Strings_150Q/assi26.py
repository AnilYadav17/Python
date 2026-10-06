'''26.Find the last occurrence of a word.'''


s = input("Enter string: ")
ch = input("Enter target: ")
result = -1  


for i in range(len(s) - len(ch) + 1):
    for j in range(len(ch)):
        if s[i+j] != ch[j]:
            break
    else:
        result = i  
        
if result != -1:
    print(f"Last occurrence found at index: {result}")
else:
    print("Target not found.")