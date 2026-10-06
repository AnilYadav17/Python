'''97. Check if two given strings appear at the end of each other (ignoring case).'''
# S1 = "abc", S2 = "Xabc" -> TRUE
s1 = input("Enter String 1: ").lower()
s2 = input("Enter String 2: ").lower()

len1 = len(s1)
len2 = len(s2)

if s2[-len1:] == s1 or s1[-len2:] == s2:
    print("TRUE")
else:
    print("FALSE")
