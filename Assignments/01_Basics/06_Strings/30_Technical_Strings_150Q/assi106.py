'''106. Generate all subsequences of a string.'''
# S = "ab" -> "", "a", "b", "ab"
s = input("Enter string: ")
subsequences = [""]

for char in s:
    current_len = len(subsequences)
    for i in range(current_len):
        subsequences.append(subsequences[i] + char)

print("Subsequences:", subsequences)
