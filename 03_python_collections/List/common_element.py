arr1 = [1, 2, 3, 3]
arr2 = [3, 1]
common = []

for i in arr1[:]:
    if i in arr2:
        arr1.remove(i)
        arr2.remove(i) 
        common.append(i)

print(common) 