'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''

code = input("Enter product code: ").lower()
if code[::-1]==code:
    print("Palindrome Code")
else:
    print("Not Palindrome Code")