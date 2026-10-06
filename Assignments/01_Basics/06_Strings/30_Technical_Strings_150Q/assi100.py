'''100. Return true if string contains 'abc' not followed by '.'.'''
# S1 = "abcx", S2 = "abc." -> S1: True, S2: False
s = input("Enter string: ")
flag = False

for i in range(len(s) - 2):
    if s[i:i+3] == "abc":
        if i + 3 == len(s) or s[i+3] != '.':
            flag = True
            break

if flag:
    print("True")
else:
    print("False")
