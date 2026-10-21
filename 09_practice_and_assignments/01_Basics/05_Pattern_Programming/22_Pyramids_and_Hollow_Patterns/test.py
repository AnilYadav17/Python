# # num = int(input())

# # i = num 
# # for i in range(1,num+1):
# #     print()
# #     j=num
# #     while j>=i:
# #         print("-",end="")
# #         j-=1



# num = int(input())

# i =num
# while i>=1:
#     print()
#     j = 1
#     while j>=num:
#         print(j,end="")
#         j+=1
#     i-=1


# # num = int(input("Enter Number:"))
# # for j in range(num*2-2,1,-2):
# #     print("_"*j)




'''
----
---
--
-
'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):
    print()
    
    for j in range(num, i, -1):
        print("-", end="")