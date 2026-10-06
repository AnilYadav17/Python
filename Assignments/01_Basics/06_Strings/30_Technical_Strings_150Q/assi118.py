'''118. Find the longest repeated substring.'''
# S = "banana" -> "ana"
s = input("Enter string: ")
longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if s.count(sub) > 1:
            if len(sub) > len(longest):
                longest = sub

print("Longest repeated substring =", longest)
