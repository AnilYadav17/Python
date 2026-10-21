'''6.Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

a = input("Enter A: ")
b = input("Enter B: ")
a = int(a,2)
b = int(b,2)
print(bin(a+b)[2:])
