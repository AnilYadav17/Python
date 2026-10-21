'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''

num = input("Enter Number = ")
sum=0
reverse=""
diff=0


for i in num:
    sum+=int(i)
    reverse=i+reverse
print("Sum of Digits =",sum)
print("Reverse =",reverse)

diff = abs(int(num)-int(reverse))
print("Difference =",diff)

result=diff+sum
print("Final Result =",result)

if result<2:
    print("Not Prime")
else:
    for i in str(result):
        if result%int(i)==0:
            print("Not Prime")
            break
    else:
        print("Prime")