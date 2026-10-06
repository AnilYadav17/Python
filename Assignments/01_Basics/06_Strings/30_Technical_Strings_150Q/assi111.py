'''111. Check if a string can be rearranged into a palindrome.'''
# S = "aabbc" -> TRUE
s = input("Enter string: ")
odd_count = 0

checked = []
for char in s:
    if char not in checked:
        checked.append(char)
        if s.count(char) % 2 != 0:
            odd_count += 1

if odd_count <= 1:
    print("TRUE")
else:
    print("FALSE")
