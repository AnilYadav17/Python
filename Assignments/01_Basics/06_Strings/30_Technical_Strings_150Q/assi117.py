'''117. Check if a string contains duplicate substrings.'''
# S = "ababa" -> True (e.g., "aba")
s = input("Enter string: ")
found = False

# Try substring lengths from 2 up to half the length of string
for length in range(2, len(s) // 2 + 1):
    for i in range(len(s) - length + 1):
        sub = s[i:i+length]
        # Check if this substring appears again later in the string
        if s.count(sub) > 1:
            print("True (e.g., \"" + sub + "\")")
            found = True
            break
    if found:
        break

if not found:
    print("False")
