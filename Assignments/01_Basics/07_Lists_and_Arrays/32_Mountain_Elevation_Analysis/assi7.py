'''7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3'''

n = int(input("Enter size of values: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Energy value: "))
    arr.append(x)

#copy
arr1= arr.copy()
factorials=[]
for i in arr1:
    factorial=1
    if i>0:
        for j in range(1,i+1):
            factorial*=j
    factorials.append(factorial)

#sum and max
sum=0
even_count=0
max=factorials[0]
for i in factorials:
    if i%2==0:
        even_count+=1
    sum+=i
    if i>max:
        max=i

print(f"""
Factorials = {factorials}
Sum = {sum}
Max = {max}
Even Count = {even_count}
""")