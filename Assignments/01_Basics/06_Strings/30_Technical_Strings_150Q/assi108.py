'''108. Check if a string is an isogram (no repeating letters).'''
# S = "ambidextrous" -> TRUE
s = input("Enter string: ").lower()
is_isogram = True

for char in s:
    if char.isalpha() and s.count(char) > 1:
        is_isogram = False
        break

if is_isogram:
    print("TRUE")
else:
    print("FALSE")
