'''104. Check if a string contains balanced brackets of all types ((), {}, []).'''
# S = "{[()]}" -> TRUE
s = input("Enter string: ")
stack = []
balanced = True

for char in s:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if len(stack) == 0:
            balanced = False
            break
        top = stack.pop()
        if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
            balanced = False
            break

if balanced and len(stack) == 0:
    print("TRUE")
else:
    print("FALSE")
