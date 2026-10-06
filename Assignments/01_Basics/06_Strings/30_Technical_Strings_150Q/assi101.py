'''101. Check if a string is a valid palindrome ignoring spaces and punctuation.'''
# S = "A man, a plan, a canal: Panama" -> TRUE
s = input("Enter string: ")
clean_s = ""

for char in s:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
        clean_s += char.lower()

if clean_s == clean_s[::-1]:
    print("TRUE")
else:
    print("FALSE")
