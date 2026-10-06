'''1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''

n= 9
num1 = 100
num2 = 200
sum=0
while num1<=num2:
    if num1%n==0:
        sum+=num1
    num1+=1
print("Sum of Numbers Divisible by 9 between 100 and 200 is :",sum)