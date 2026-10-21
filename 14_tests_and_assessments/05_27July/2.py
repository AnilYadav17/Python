'''
problem 2:-   3 marks

Matrix Multiplication

Write a Python program to read two matrices from the user and perform matrix multiplication.

Before multiplying the matrices, check whether multiplication is possible. Matrix multiplication is possible only if
the number of columns in the first matrix is equal to the number of rows in the second matrix.

Requirements
Read the number of rows and columns for the first matrix.
Read all the elements of the first matrix from the user.
Read the number of rows and columns for the second matrix.
Read all the elements of the second matrix from the user.
Check whether matrix multiplication is possible.
If possible, multiply the matrices using nested loops.
Display the resulting matrix.

If multiplication is not possible, display:

Matrix multiplication is not possible.
'''

r1,c1 = map(int,input("Enter First Matrix Row and Columns Size: ").split())
r2,c2 = map(int,input("Enter Second Matrix Row and Columns Size: ").split())

if c1 == r2:
    print("\nMatrix 1:")
    matrix1 =[]
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input(f"Enter Matrix1 {j+1} element: ")))
        matrix1.append(row)
        
    print("\nMatrix 2:")
    matrix2 =[]
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input(f"Enter Matrix2 {j+1} element: ")))
        matrix2.append(row)
    
    print(matrix1,"\n",matrix2)
    
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            val = 0
            for k in range(c1):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)
        
    print("\nResultant Matrix:")
    for row in result:
        for val in row:
            print(val, end=" ")
        print()
    
else:
    print("\n Matrix Multiplication Not Possible")
