'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2'''

#while loop
# n = int(input("Enter a number = "))
# smallest = 9
# while n>0:
#     digit=n%10
#     if digit<smallest:
#         smallest=digit
#     n//=10
# print("Smallest Digit = ",smallest)


#for loop
n = input("Enter a number = ")
smallest = 9
for digit in n:
    digit=int(digit)
    if digit<smallest:
        smallest=digit
print("Smallest Digit =",smallest)
