'''89. Remove 'b' and 'ac' from a string.'''

s = input("Enter string: ")
result=" "

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         result +=s[i:j+1] +" "


for i in range(len(s)):
    if i==0:
        if s[i]!="b" and s[i]+s[i+1]!="ac":
            result+=s[i]
    elif i==len(s)-1:
        if s[i]!="b" and s[i-1]+s[i]!="ac":
            result+=s[i]
    else:
        if s[i]!="b" and s[i]+s[i+1]!="ac":
            result+=s[i]

print(result)


# i = 0
# while i < len(s):

#     if s[i] == 'b':
#         i += 1

#     elif i < len(s)-1 and s[i] + s[i+1] == "ac":
#         i += 2

#     else:
#         result += s[i]
#         i += 1

# print(result)