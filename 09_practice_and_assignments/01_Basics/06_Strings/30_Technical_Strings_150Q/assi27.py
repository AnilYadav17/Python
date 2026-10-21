'''27.Find the last occurrence of a word.'''


s = input("Enter String: ")  # Example: "Test this test "
ch = input("Enter Target: ")  # Example: "test"

result = -1  

for i in range(len(s) - len(ch), -1, -1):
    for j in range(len(ch)):
        if s[i+j] != ch[j]:
            break
    else:
        result = i + len(ch) - 1
        break  
        
if result != -1:
    print(f"Last occurrence found at index: {result}")
else:
    print("Target not found.")