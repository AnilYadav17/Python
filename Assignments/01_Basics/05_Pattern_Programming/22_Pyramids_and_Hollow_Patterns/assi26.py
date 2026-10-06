'''
26) Right Hollow Number Triangle
1
12
1 3
1  4
12345'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    for numbers in range(1,i+1):
        if  numbers==1 or numbers==i or i==num:
            print(numbers,end="")
        else:
            print(" ",end="")
    print()