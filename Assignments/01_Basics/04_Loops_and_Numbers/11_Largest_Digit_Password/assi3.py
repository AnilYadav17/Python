'''3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''

n= input("Enter Number = ")
digit = ""

for i  in n:
    digit=i
    break
print("First Digit = ",digit)




# n = input("Enter ID = ")
# p = len(n)
# n = int(n)
# n=n//10**(p-1)
# print(n)