# arr = [1,2,3,4]
# odd=[]
# even=[]

# for i in arr:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(odd,even)

arr = [12,2,3,4]
arr1= [3,14,12]
common=[]

for i in arr:
        if i in arr1 and i%2==0 and i>10:
            common.append(i)

print(common)