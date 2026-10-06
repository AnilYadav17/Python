'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''

num,power=map(int,input("Enter Number and Power = ").split())
result= 1
for i in range(power):
    result *= num
print("Value = ",result)

