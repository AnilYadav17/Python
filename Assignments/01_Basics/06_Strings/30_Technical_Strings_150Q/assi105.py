'''105. Find the longest valid parentheses substring.'''
# S = ")()())" -> 4
s = input("Enter string: ")
max_len = 0

for i in range(len(s)):
    for j in range(i + 2, len(s) + 1, 2):
        sub = s[i:j]
        # Validate substring parentheses balance
        count = 0
        valid = True
        for char in sub:
            if char == '(': count += 1
            elif char == ')': count -= 1
            if count < 0:
                valid = False
                break
        if valid and count == 0:
            if len(sub) > max_len:
                max_len = len(sub)

print("Longest valid length =", max_len)
