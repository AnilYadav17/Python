'''110. Find the lexicographically largest substring of length k.'''
# S = "banana", k = 3 -> "nan"
s = input("Enter string: ")
k = int(input("Enter length k: "))

largest = s[0:k]
for i in range(1, len(s) - k + 1):
    sub = s[i:i+k]
    if sub > largest:
        largest = sub

print("Lexicographically largest =", largest)
