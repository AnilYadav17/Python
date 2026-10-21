'''4. Longest Consecutive Sequence

Scenario
Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3'''

#Taking input from userlen(arr)
n = int(input("Enter length of sequence: "))
arr1=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr1.append(x)
arr1.sort()

count=1
flag=True
for i in range(len(arr1)):
    if i==0:
        if arr1[i]+1==arr1[i+1]:
            count+=1
        else:
            flag=False
            break
    elif i==len(arr1)-1:
        pass
    #     if arr1[i]-1==arr1[i-1]:
    #         count=+1
    #     else:
    #         flag=False
    else:
        if arr1[i]+1==arr1[i+1]:
            count+=1
        else:
            break
print(count)
















# #count
# count=1
# if n>1:
#     for i in range(len(arr)):
#         if i==0:
#             if arr[i]+1==arr[i+1]:
#                 count+=1
#         elif i==len(arr)-1:
#             if arr[i]==arr[i-1]+1:
#                 count+=1
#         else:
#             if arr[i]+1==arr[i+1]:
#                 count+=1
#             else:
#                 break
# print(count)


