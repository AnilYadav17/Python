'''44.Check if two strings are anagrams.'''


s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
visited=[]
flag=0


if len(s1)!=len(s2):
    flag=0
else:
    for i in range(len(s1)):
        if s1[i] not in s2 and s2[i] not in s1:
            flag=0
        else:
            flag=1

if flag==1:
    print("Both strings are anagram")
else:
    print("Both strings are not anagram")