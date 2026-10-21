'''5.Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145'''


num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
print("Strong Numbers are: ")


while num1<=num2:
    org = num1
    sum=0
    while org>0:
        digit=org%10
        fact=1
        i=1
        while i<=digit:
            fact=fact*i
            i+=1
        sum=sum+fact
        org=org//10
    if num1==sum:
        print(num1)
    num1+=1




# for i in range(num1,num2+1):
#     for j in str(num1):
#         fact=1
#         for k in range(1,int(j)+1):
#             fact=fact*int(k)
#         sum=sum+fact
#         print(sum,fact)
