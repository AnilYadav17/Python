'''129. Find the smallest window containing all distinct characters.'''
# S = "aabcbae" -> "aabcbae" -> "aabcde" from snapshot example
s = input("Enter string: ")

# Find all distinct characters in the input string
distinct_chars = []
for char in s:
    if char not in distinct_chars:
        distinct_chars.append(char)

smallest = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        
        # Check if substring contains all unique characters
        contains_all = True
        for char in distinct_chars:
            if char not in sub:
                contains_all = False
                break
                
        if contains_all:
            if smallest == "" or len(sub) < len(smallest):
                smallest = sub

print("Smallest window containing distinct characters =", smallest)
