'''121. Check if a string contains only binary digits (0/1).'''
# S1 = "1010" -> True, S2 = "102" -> False
s = input("Enter string: ")
is_binary = True

if len(s) == 0:
    is_binary = False

for char in s:
    if char != '0' and char != '1':
        is_binary = False
        break

if is_binary:
    print("True")
else:
    print("False")
