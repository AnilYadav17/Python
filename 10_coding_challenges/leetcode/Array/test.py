# nums = [[-4,-1,0,3,10],[-4,-1,0,3,10]]
# ans = []
# # nums = set(nums)
# print(nums)

# nums= [3,2,1,4,5,6,7]
# i,j,k=0,1,2

# print(sorted([nums[i],nums[j],nums[k]]))

# # for i in nums:
# #     ans.append(i)
# #     ans.append(i)
# print(float("inf"))
# # print(sum(nums))
# # print(nums)


# nums = [1,1,1,1,1,1,1]

# for i in nums[:]:
#     if i==1:
#         i=2

# print(nums)

# nums = [1,2,3,4,5,6]
# print([0]*len(nums))

# s  = "Flower Flight Flow"
# s = s.split() #["Flower","Flight","Flow"]
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         if s[i][j] != s[i+1][j]:
#             break
#         else:
#             if s[i][j+1] == s[i+1][j+1]:
                
# def abstract(x,y):
#     return abs(x-y)

# print(abs(sum([1,2,3,-4,-5])))

# from functools import reduce

# def add(x,y):
#     return x+y


# def addition(*args):
#     nums = list(args)
#     return reduce(add,nums)


# print(addition(10,20,30))

# def display(name,age,*,marks):
#     print(name)
#     print(age)
#     print(marks)

    

# display("Anil",17,marks=100)

# from functools import reduce
# result =lambda a,b: a if a>b else b
# print(result(2,3))

# def add(x,y):
#         return x+y
# nums = [10,20,30,43,50]
# result = reduce(add,nums)
# print(result)
# def sum(x,y):
#     return   x+y

# def square(x):
#     return x**2

# def both(a,b):
#     return square(sum(a,b))
# print(both(10,20))


# def outer():
#     x =100
#     def inner():
        
#         return x
#     print(inner())
# print(outer())


# def outer(name):
#     msg = f"hiiiiiii {name}"
#     def inner():
#         print(msg)
#     return inner
# o = outer("bhumika")
# o()


# def counter():
#     x=0
#     def increment():
#         x+=1
#         print(x)
#     return increment

# c = counter()
# c()
# c()
# c()

# def greet(greeting,name):
#     def card():
#         g = f"{greeting},{name}"
#         return g    
#     return card


# x = greet("Anill","Yadav")
# print(x())

# import time
# import os
# print("Hiii")
# time.sleep(2)
# print("Hlw after 2 Sec")

# time.sleep(5)
# os.system("clear")

'''86.Print all permutations of a string without repetition.'''

s = input("Enter string: ")
used=[]
result=""

for i in s:
    for j in s:
        if i!=j:
            result+=i+j+" "

    if result not in used:
        used.append(result)
print(result)