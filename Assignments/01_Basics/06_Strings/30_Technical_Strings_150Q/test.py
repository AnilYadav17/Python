
# s = input("Enter string:")
# ch = input("Enter char: ")
# count=0


# for i in range(len(s)-len(ch)+1):
#     match=True
#     for j in range(len(ch)):
#         if ch[j]!=s[i+j]:
#             match=False
#             break
#     if match==True:
#         count+=1

# print(count)

# s1 = "ab"
# l = list(s1)
# print(l)

# s="Anil"
# print(s[2:])


# students = ["deepika","rashmika","katappa"]
# name= input("Enter name:")
# if name in students:
#     index=students.index(name)
#     students[index]=name.upper()
#     print(students)
# else:
#     print("Student not found")

# print(ord("t"))


# s = input("Enter string: ")
# stack=""
# for i in s:
#     if len(stack)>0 and stack[-1]==i:
#         stack=stack[:-1]
#     else:
#         stack+=i

# print(stack) 

s = input("Enter string:")
l = s.split()
unique=[]
#unique
for i in l:
    if i not in unique:
        unique.append(i)

counts=""
for i in l:
    count=0
    for j in l:
        if i==j:
            count+=1
    counts+=str(count)

for i,j in zip(unique,counts):
    print(i,j)