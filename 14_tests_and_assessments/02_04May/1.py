'''1.
Digit Frequency Balance Analyzer

A data security system analyzes numeric IDs to check digit distribution patterns.

For a given number, the system evaluates how frequently each digit appears.

Write a program to:

Count how many times each digit appears in the number
Display only the digits that appear more than once
Find the total count of repeated digits
Find the digit with maximum frequency
If no digit repeats, print Unique Number
If at least one digit repeats, print Repeated Pattern Detected

Use loops wherever required.

Input:
1223451

Output:
Repeated Digits: 1 2
Total Repeated Count = 4
Max Frequency Digit = 1
Repeated Pattern Detected'''


num = input("Enter Number: ")
real_result=""
dup_result=""

for i in num:
    count=0
    for j in num:
        if i==j:
            count+=1
    if count>1:
        dup_result+=i

for i in dup_result:
    for j in dup_result:
        if j not in real_result:
            real_result+=j+" "


largest = ""
maximum = 0
for i in real_result.split():

    count = 0

    for j in num:
        if i == j:
            count += 1

    if count > maximum:
        maximum = count
        largest = i
    
if dup_result == "":
    print("Unique Number")

else:
    print("Repeated Digits:", real_result)
    print("Total Repeated Count =", len(dup_result))
    print("Max Frequency Digit =", largest)
    print("Repeated Pattern Detected")