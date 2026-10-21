# s = input("Enter String:")

# result = ""

# for x in s:
#     if x.isalpha():
#         result = result+x
#         previous=x
#     else:
#         newch = chr(ord(previous)+int(x))
#         result = result+newch

# print(result)


s = input("Enter String: ")
ls = s.split()
result = ""

for i in range(len(ls)-1, -1, -1):
    result=result+ ls[i]+" "

print(result)