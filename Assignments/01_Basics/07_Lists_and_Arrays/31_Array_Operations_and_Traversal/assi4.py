'''4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''


#numbers from user
n = int(input("Enter number of numbers : "))
arr=[]
for i in range(n):
    x = int(input(f"number{i+1}: "))
    arr.append(x)

palindromes_count=0

count=0
sorted_palindrome=0
palindromes=[]
for i in arr:
    if str(i)==str(i)[::-1]:
        palindromes.append(i)
        count+=1

largest=palindromes[0]
for i in palindromes:
    if i>largest:
        largest=i

print(f"""Palindromes: {palindromes}
Count: {count}
Largest: {largest}
Sorted: {sorted(palindromes)}'''

""")