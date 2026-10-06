'''3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output: e'''

s1 = input("Enter String: ").lower()
found = 0

for i in s1:
    count = 0

    for j in s1:
        if i == j:
            count += 1

    if count == 1:
        print("First Non Repeated character:", i)
        found = 1
        break

if found == 0:
    print("No non repeated character found")