arr=[10,20,40,50,5,8,30]

max=arr[0]
min=arr[0]

for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i

print(min,max)