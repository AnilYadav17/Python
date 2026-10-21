'''4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number'''

num = int(input("Enter Number = "))
n = 0
diff = 0
count = 0

max=0
difference =""
for i in str(num):
    if n==0:
        n = int(i)
    else:
        diff = abs(n-int(i))
        flag=0
        n=int(i)
        difference = difference+" "+str(diff)
        if diff>=2:
            flag=1
        if int(i)>2:
            count+=1
        if max<diff:
            max=diff

print("Differences:",difference)
print("Count (>2) =",count)
print("Max Difference =",max)
if flag==1:
    print("Smooth Number")
else:
    print("Not Smooth Number")