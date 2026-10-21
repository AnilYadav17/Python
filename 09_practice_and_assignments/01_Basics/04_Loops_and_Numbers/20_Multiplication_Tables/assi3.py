'''3.Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47'''


num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))

while num1<=num2:
    i=2
    while i<num1//2+1:
        if num1%i==0:
            break
        i+=1
    else:
        print(num1)
    num1+=1