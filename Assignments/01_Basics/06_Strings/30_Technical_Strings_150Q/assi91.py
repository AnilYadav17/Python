'''91 Check if two strings are interleaving of another string.
#S1 = "aab", S2 = "axy",    ->    S3 = "aaxaby"'''

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
S = input("Enter main String: ")
flag=True
visited=""
s = s1+s2
if len(s)!=len(S):
    flag=False
else:
    s=sorted(s)
    S=sorted(S)
    for i in s:
        if s.count(i)!=S.count(i):
            flag=False

print(flag)            
