'''7.Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9'''


num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
print("Neon Numbers are: ")


while num1<=num2:
    square = num1*num1
    sum=0
    while square>0:
        digit = square%10
        sum=sum+digit
        square=square//10
    if num1==sum:
        print(num1)
    num1+=1