'''5. Equilibrium Index Finder


Scenario
Find an index where:

# Sum of elements on the left side = Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found'''


#Taking input from userlen(arr)
n = int(input("Enter length of sequence: "))
arr1=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr1.append(x)
arr=arr1.copy()


#equilibrium  index = sum of all left elements == sum of all right elements
# equilibrium_index=-1
# left_sum=0
# right_sum=0

# for i in arr:
#     if i==0 and n==1:
#         equilibrium_index=i
#         break
#     if i==0:
#         left_sum+=1
#     elif i==len(arr)-1:
#         right_sum+=1
#     else:
#         for j in range(len(arr)-1,-1,i):
#             left_sum+=1
#         if left_sum==right_sum:
#             print(left_sum,right_sum)



equilibrium_index = -1

for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i+1:])

    if left_sum == right_sum:
        equilibrium_index = i
        break

if equilibrium_index != -1:
    print("Equilibrium Index =", equilibrium_index)
else:
    print("No Equilibrium Index Found")

