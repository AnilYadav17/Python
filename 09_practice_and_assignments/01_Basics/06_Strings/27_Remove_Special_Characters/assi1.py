'''1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System
A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.
Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output:
AjaySingh'''

str1 = input("Enter String: ")
result=""

for i in str1:
    if (i>="a" and i<="z") or (i>="A" and i<="Z") or (i>="0" and i<="9") or i==" ":
        result+=i

print(result)