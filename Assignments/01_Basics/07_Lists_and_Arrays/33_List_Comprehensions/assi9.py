'''9. Happy Number List Analyzer
=============================

Scenario

Store numbers in a list and identify Happy Numbers.

A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.

Example

19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

Therefore, 19 is a Happy Number.

Another Example

7

7² = 49

4² + 9² = 97

9² + 7² = 130

1² + 3² + 0² = 10

1² + 0² = 1

Therefore, 7 is a Happy Number.

Non-Happy Number Example

4

4² = 16

1² + 6² = 37

3² + 7² = 58

5² + 8² = 89

8² + 9² = 145

1² + 4² + 5² = 42

4² + 2² = 20

2² + 0² = 4

Again 4 appears and the cycle repeats.

Therefore, 4 is NOT a Happy Number.

Requirements

* Read N and list elements from user
* Find all Happy Numbers
* Store Happy Numbers in another list
* Count Happy Numbers
* Find Largest Happy Number
* Display Happy Number List

Test Case 1

Input:
[19, 7, 4, 20]

Output:
Happy Numbers = [19, 7]
Count = 2
Largest Happy Number = 19

Test Case 2

Input:
[13, 10, 4]

Output:
Happy Numbers = [13, 10]
Count = 2
Largest Happy Number = 13

Test Case 3

Input:
[2, 3, 4]

Output:
Happy Numbers = []
Count = 0
Largest Happy Number = Not Available

---'''


# a = 49
# sum = 0
# for i in str(a):
#     sum+=int(i)**2

# for j in str(sum):
#     if len(str(sum))>1:
#         sum+=int(i)**2
#     else:
#         if j==1:
#             print("Happy")
#         else:
#             print("Not Happy")

# a = 49
# total_sum = 0
# for i in str(a):
#     total_sum += int(i)**2

# for j in str(total_sum):
#     if len(str(total_sum))>1:
#         temp_sum = 0 
#         for digit in str(total_sum):
#             temp_sum += int(digit)**2
#         total_sum = temp_sum
#     else:
#         if j == "1":
#             print("Happy")
#             break
#         else:
#             print("Not Happy")
#             break

# #Taking input from user
# n = int(input("Enter length of numbers: "))
# arr=[]
# for i in range(n):
#     x=int(input(f"{i+1}. Elemenet: "))
#     arr.append(x)

# happy_numbers=[]
# for a in arr:
#     total_sum = 0
#     for i in str(a):
#         total_sum += int(i)**2

#     for j in str(total_sum):
#         if len(str(total_sum))>1:
#             temp_sum = 0 
#             for digit in str(total_sum):
#                 temp_sum += int(digit)**2
#             total_sum = temp_sum
#         else:
#             if j == "1":
#                 happy_numbers.append(a)
#                 break
#             else:
#                 break
            
# print(happy_numbers)


# Taking input from user
n = int(input("Enter length of numbers: "))

arr = []
for i in range(n):
    x = int(input(f"{i+1}. Element: "))
    arr.append(x)

happy_numbers = []

for num in arr:
    current = num
    visited = []


happy_numbers = []

for num in arr:
    current = num
    visited = []
    while current != 1 and current not in visited:
        visited.append(current)

        total_sum = 0
        for digit in str(current):
            total_sum += int(digit) ** 2

        current = total_sum

    if current == 1:
        happy_numbers.append(num)

print("Happy Numbers:", happy_numbers)