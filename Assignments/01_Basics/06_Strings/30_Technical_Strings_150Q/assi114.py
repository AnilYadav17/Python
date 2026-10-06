'''114. Check if one string is a subsequence of another.'''
# S1 = "ace", S2 = "abcde" -> TRUE
s1 = input("Enter string 1 (subsequence): ")
s2 = input("Enter string 2 (main string): ")

i, j = 0, 0
while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        i += 1
    j += 1

if i == len(s1):
    print("TRUE")
else:
    print("FALSE")
