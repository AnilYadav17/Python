'''4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d'''


s = input("Enter string: ")
result=""
max=0
output=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count==1 or i not in result:
        result+=i
    if max<=count:
        max=count
        output+=i


        