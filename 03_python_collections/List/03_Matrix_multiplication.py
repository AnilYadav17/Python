m1 = [
    [1,2,3],
    [4,5,6]
]

m2 = [
    [8 ,7],
    [6, 5],
    [4, 3]
]

result=[]
for i in range(len(m1)): #r1
    row=[]
    for j in range(len(m2[i])): #c2
        row.append(0)
    result.append(row)

for i in range(len(m1)): #r1
    for j in range(len(m2[i])): #c2
        for k in range(len(m1[i])): #c1
            result[i][j]+=m1[i][k]*m2[k][j]

print(result)



# r1 = int(input("Number of Rows1: "))
# c1 = int(input("Number of columns1: "))
# matrix1=[]
# #taking input elements from user for matrix1
# for i in range(r1):
#     row=[]
#     for j in range(c1):
#         row.append(int(input(f"{j+1} Element: ")))
#     matrix1.append(row)

# r2 = int(input("Number of Rows2: "))
# c2 = int(input("Number of columns2: "))
# matrix2=[]
# for i in range(r2):
#     row=[]
#     for j in range(c2):
#         row.append(int(input(f"{j+1} Element: ")))
#     matrix2.append(row)


# result=[]
# for i in range(len(m1)): #r1
#     row=[]
#     for j in range(len(m2[i])): #c2
#         row.append(0)
#     result.append(row)

# for i in range(len(m1)): #r1
#     for j in range(len(m2[i])): #c2
#         for k in range(len(m1[i])): #c1
#             result[i][j]+=m1[i][k]*m2[k][j]

# print(result)
