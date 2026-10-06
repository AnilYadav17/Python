'''45. Check whether a string starts/ends with another string.'''

s1 = input("Enter string1: ")
p = input("Enter prefix: ")
s = input("Enter suffix: ")

len_s1 = len(s1)
len_p = len(p)
len_s = len(s)
prefix_match=True
suffix_match=True


# Length check
if len_p > len_s1 or len_s > len_s1:
   pass

else:

    # Check prefix
    for i in range(len_p):
        if s1[i] != p[i]:
            prefix_match=False
            break

    # Check suffix
    if s1[-len_s:] != s:
        suffix_match=False


print(f"Prefix match: {prefix_match} , Suffix match: {suffix_match}")
