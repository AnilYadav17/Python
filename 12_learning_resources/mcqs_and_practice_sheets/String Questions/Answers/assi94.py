'''94. Find the smallest window containing all characters of another string'''
#S1 = "ADOBECODEBANC", S2 = "ABC"   -> "BANC"



s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

smallest = ""

for i in range(len(s1)):
    for j in range(i, len(s1)):

        sub = s1[i:j+1]

        found = True

        for ch in s2:
            if ch not in sub:
                found = False
                break

        if found:
            if smallest == "" or len(sub) < len(smallest):
                smallest = sub

if smallest:
    print("Smallest Window =", smallest)
else:
    print("No window found")