'''2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output = 4'''


n = int(input("Enter the size of strings: "))

passwords=list(input("Enter Passwords: ").split(","))

count=0
for i in range(n):
    for j in range(i+1,n):
        flag=True
        for k in passwords[i]:
            if k in passwords[j]:
                flag=False
                break
        if flag:
            count+=1
print(count)