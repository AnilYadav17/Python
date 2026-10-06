# rows = int(input("Enter number of Rows: "))
# cols = int(input("Enter number of columns: "))
# matrix1=[]

# #taking input elements from user for matrix1
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input(f"{j+1} Element: ")))
#     matrix1.append(row)


# #accessing element column vise
# for i in range(len(matrix1[i])):
#     for j in range(len(matrix1)):
#         for k in range()
#         if matrix1[j][i]:


# arr = [1,3,4,6,8,9]

# for i in arr:
#     count=0
#     if i>2:
#         for j in range(2,i):
#             if i%j==0:
#                 count+=1
#     print(i,count)

arr = [6,10, 12, 20 ,80 , 70, 85, 15]
perfects=[]
for i in arr:
    d_sum=0
    for j in range(1,i):
        if i%j==0:
            d_sum+=j
    if d_sum==i:
        perfects.append(i)
print(perfects)


