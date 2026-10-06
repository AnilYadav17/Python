# results = {
#     "Ajay": 88,
#     "Ravi": 45,
#     "Neha": 76,
#     "Aman": 39
# }

# passing_marks = 50

# for i,j in results.items():
#     if j>=50:
#         print(i,end=" ")
# print()


# emails = [
#     "ajay@gmail.com",
#     "ravi@yahoo.com",
#     "neha@gmail.com",
#     "aman@outlook.com",
#     "abc@gmail.com"
# ]


# result={}

# for i in emails:
#     if i    


s = input("Enter string: ")
r = ""

for i in range(len(s)):
    if s[i]!=" ":
        r=s[i]+r
    else:
        print(r,end=" ")
        r=""

print(r)