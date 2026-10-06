'''60.Append two strings but remove adjacent duplicates.'''
#miss+issue = missue

s1 = input("Enter string: ")
s2 = input("Enter second string: ")
result=s1
for i in range(len(s2)):
    if i == 0 and len(result) > 0:
        if result[-1] == s2[i]:
            continue
    result += s2[i]
print(result)


# s1 = input("Enter string: ")
# s2 = input("Enter second string: ")
# result = s1
# for i in range(len(s2)):
#     if len(result) > 0 and result[-1] == s2[i]:
#         continue   
#     result += s2[i]
# print(result)


# s1 = input("Enter string: ")
# s2 = input("Enter second string: ")
# result = s1
