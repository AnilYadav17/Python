'''120. Find the longest substring containing only vowels.'''
# S = "abaeiouy" -> "aeiou"
s = input("Enter string: ")
vowels = "aeiouAEIOU"
longest = ""
current = ""

for char in s:
    if char in vowels:
        current += char
        if len(current) > len(longest):
            longest = current
    else:
        current = ""

print("Longest vowel-only substring =", longest)
