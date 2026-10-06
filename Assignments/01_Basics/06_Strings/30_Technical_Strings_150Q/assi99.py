'''99. Check if a 'z' is happy (surrounded by same chars).'''
# S = "azzb" -> FALSE
s = input("Enter string: ")
is_happy = True
found_z = False

for i in range(len(s)):
    if s[i] == 'z':
        found_z = True
        if i == 0 or i == len(s) - 1 or s[i-1] != s[i+1]:
            is_happy = False
            break

if found_z and is_happy:
    print("TRUE")
else:
    print("FALSE")
