'''47.Check for substring using concatenation trick.'''
#Input: S1="CDAB", S2="ABCD"  , Output:True (S1 is in S2+S2)

s1 = input("Enter string to check: ")
s2 = input("Enter string: ")

if s1 not in s2+s2:
    print("False")
else:
    print("True") 