'''15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *'''

# num = int(input("Enter Number: "))
# for i in range(1,num+1):
#     print()
#     for j in range(1,num*2):
#         if i==j and i%2!=0 or j-i==num-1 and j%2!=0  :
#           print("*",end="")
#         else:
#           print(" ",end="")

num = int(input("Enter Number: "))

for i in range(1, num + 1):
    for j in range(1, num * 2):

        if i == j or j - i == num - 1 or i - j == num - 1 or i + j == num * 2:
            print("*", end="")

        else:
            print(" ", end="")

    print()