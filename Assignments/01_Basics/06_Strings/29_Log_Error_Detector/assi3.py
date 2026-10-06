'''# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print: No unique digit found


Input: A122334455667789

Output: 8
'''

s = input("Enter String: ")
count=0
f = 0

for i in s:
    if i not in s:
        count+=1
        f=1
if f==0:
    print("No unique character found")
else:
    print("Count ",count)

