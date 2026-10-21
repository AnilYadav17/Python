n = int(input("Enter the size of matrix: "))

matrix = []
print("\nEnter matrix elements:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(*(str(val) for val in row))

# Main Diagonal elements
main_diagonal = [matrix[i][i] for i in range(n)]
print("\nMain Diagonal Elements:")
print(*(str(val) for val in main_diagonal))

# Secondary Diagonal elements
secondary_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
print("\nSecondary Diagonal Elements:")
print(*(str(val) for val in secondary_diagonal))

# Create transpose without zip() or numpy
transpose_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    transpose_matrix.append(row)

print("\nTranspose Matrix:")
for row in transpose_matrix:
    print(*(str(val) for val in row))

# Swap each main diagonal element with the corresponding secondary diagonal element
final_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(transpose_matrix[i][j])
    final_matrix.append(row)

for i in range(n):
    final_matrix[i][i], final_matrix[i][n - 1 - i] = final_matrix[i][n - 1 - i], final_matrix[i][i]

# Display final matrix
print("\nFinal Matrix After Diagonal Swapping:")
for row in final_matrix:
    print(*(str(val) for val in row))