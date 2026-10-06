'''107. Check if a string is a pangram (contains every letter).'''
# S = "The quick brown fox jumps over the lazy dog" -> TRUE
s = input("Enter string: ").lower()
is_pangram = True

for i in range(26):
    char = chr(ord('a') + i)
    if char not in s:
        is_pangram = False
        break

if is_pangram:
    print("TRUE")
else:
    print("FALSE")
