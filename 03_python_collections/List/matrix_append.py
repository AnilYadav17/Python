rows= int(input())
col = int(input())

matrix=[]

for i in range(rows):
	row=[]
	for j in range(col):
		row.append(int(input()))
	matrix.append(row)

print(matrix)
