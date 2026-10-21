'''98. Check if the first 'z' is immediately followed by another 'z'.'''
# S1 = "zzyy", S2 = "zyzz" -> S1: True, S2: False
s = input("Enter string: ")
idx = s.find('z')

if idx != -1 and idx < len(s) - 1:
    if s[idx + 1] == 'z':
        print("True")
    else:
        print("False")
else:
    print("False")
