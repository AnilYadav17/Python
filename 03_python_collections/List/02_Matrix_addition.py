rows = int(input("Enter number of Rows: "))
cols = int(input("Enter number of columns: "))

matrix1=[]
#taking input elements from user for matrix1
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input(f"{j+1} Element: ")))
    matrix1.append(row)


matrix2=[]
#taking input elements from user for matrix1
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input(f"{j+1} Element: ")))
    matrix2.append(row)

#                                       Using  ZIP
# matrix3=[]
# for row1,row2 in zip(matrix1,matrix2):
#     row=[]
#     for j,k in zip(row1,row2):
#         row.append(j+k)
#     matrix3.append(row)


#                                       Using 0 Append
# matrix3=[]
# for i in range(rows):
#     row=[]
#     for j in range(len(matrix1[i])):
#         row.append(0)
#     matrix3.append(row)
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         matrix3[i][j]=matrix1[i][j]+matrix2[i][j]

#                                       Without Using 0 Append
matrix3=[]
for i in range(rows):
    row=[]
    for j in range(len(matrix1[i])):
        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)


#Displaying the matrix
print()
print("Resultant Matrix: ")
for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        print(matrix3[i][j],end=" ")
    print()
