rows = int(input("Enter number of Rows: "))
cols = int(input("Enter  number of columns:"))

matrix=[]
sum=0
for i in range(rows):
	row=[]
	for j in range(cols):
		x=int(input(f"Enter {j+1} element: "))
#		sum+=x
		row.append(x)
	matrix.append(row)


i=0
while len(matrix)>i:
	j=0
	while j<len(matrix[i]):
		sum+=matrix[i][j]
		j+=1
	i+=1
print("Sum of all elements:",sum)
#print(matrix)

