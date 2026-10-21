'''90.Remove adjacent duplicates recursively.'''
#abzxxzy -> aby

s = input("Enter string: ")
stack = ""

# for i in s:
#     if len(stack) > 0 and stack[-1] == i:
#         stack = stack[:-1]   # remove duplicate
#     else:
#         stack += i           # add character

# print(stack)


for i in s:
    if len(stack)>0 and stack[-1] == i:
        stack=stack[:-1] 
    else:
        stack+=i