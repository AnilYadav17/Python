'''119. Find the smallest substring containing all vowels.'''
# S = "aeiouy" -> "aeiou"
s = input("Enter string: ")
vowels = "aeiou"
smallest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        # Check if all vowels are present
        has_all = True
        for v in vowels:
            if v not in sub.lower():
                has_all = False
                break
        if has_all:
            if smallest == "" or len(sub) < len(smallest):
                smallest = sub

print("Smallest substring with all vowels =", smallest)
