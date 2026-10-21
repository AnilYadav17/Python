rows = int(input("Enter number of Rows: "))
cols = int(input("Enter number of columns: "))
matrix=[]


#taking input elements from user
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input(f"{j+1} Element: ")))
    matrix.append(row)


#Displaying the matrix
print()
print("Original Matrix: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()

print()
#Displaying maximum and minimum
max=matrix[0][0]
min=matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]>max:
            max = matrix[i][j]
        if  matrix[i][j]<min:
            min = matrix[i][j]

#sum
sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum+=matrix[i][j]

#diagonal digits sum
d_sum=0
for i in range(len(matrix)):
        d_sum+=matrix[i][i]

#odd sum
odd_sum=0
for i in matrix:
    for j in i:
        if j%2!=0:
            odd_sum+=j

# rev_matrix=[]
# for i in range(len(matrix)):
#     rev_matrix.append(matrix[i][::-1])
# print()

rev_matrix=matrix.copy()
for row in rev_matrix:
    i=0
    j=len(row)-1
    while i<j:
        temp=row[i]
        row[i]=row[j]
        row[j]=temp
        i+=1
        j-=1



print("Reverse Matrix: ")
for i in range(len(rev_matrix)):
    for j in range(len(rev_matrix[i])):
        print(rev_matrix[i][j],end=" ")
    print()
print()


print(f"Maximum: {max}\nMinimum: {min}")
print(f"Sum : {sum}\nAverage : {sum/(rows*cols)}")
print(f"Diagonal Sum: {d_sum} \nOdd Sum: {odd_sum}")
