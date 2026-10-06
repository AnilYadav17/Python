'''4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.'''


# n = int(input("Enter number of Arrays: "))
# main = []
# for i in range(n):
#     print(f"Enter {i+1} row elements: ")
#     main.append(list(map(int, input().split())))

# common = []
# if n > 0:
#     prev = None
#     for value in main[0]:
#         if value == prev:
#             continue
#         prev = value

#         found = True
#         for arr in main[1:]:
#             if value not in arr:
#                 found = False
#                 break

#         if found:
#             common.append(value)

# print(common)



a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
c = list(map(int, input("Enter third array: ").split()))

ans = []

for x in a:
    if x in b and x in c and x not in ans:
        ans.append(x)

print("Common elements:", ans)