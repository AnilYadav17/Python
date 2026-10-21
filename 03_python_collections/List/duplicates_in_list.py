arr = [1,2,2,3,4 ,4]
unique=[]
for i in range(len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])
arr=unique

# print(unique)


# for i in arr:
#     count=0
#     for j in arr:
#         if i==j:
#             count+=1
#     if count>1:
#         arr.remove(i)
# print(arr)

#second largest

arr.sort()
print(arr[-2])

