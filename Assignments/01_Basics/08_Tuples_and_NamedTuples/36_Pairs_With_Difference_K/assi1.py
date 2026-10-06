'''1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)

'''

n = int(input("Enter number of ages: "))
k = int(input("Enter the difference: "))
arr=list(map(int,input("Enter ages :").split(",")))

#counting the pairs with given difference
count=0
for i in range(n):
    for j in range(i+1,n):
        if abs(arr[i]-arr[j])==k:
            count+=1

print(f"Pairs with {k} difference : {count}")