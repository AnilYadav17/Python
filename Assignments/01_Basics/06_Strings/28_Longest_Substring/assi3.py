'''3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda'''

s = input("Enter string: ")
result=""

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count==1 or i not in result:
        result+=i
    else:
        pass
print(result)