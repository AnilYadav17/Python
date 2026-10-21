'''
6.

 Frequency Count of Elements (Advanced Scenario-Based Problem)


A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

The department wants to analyze:

* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)

---

 Requirements

Write a Python program to:

1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary

---


NOTE:
* Avoid using built-in `Counter`

## Input Format

A list of integers representing responses.

---

# Scenario 1: Normal Survey Data

## Input

[1, 2, 2, 3, 3, 3, 4, 1, 2]

## Output

```
Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1

Most Frequent: 2 or 3 (tie)
Least Frequent: 4
```

---

# Scenario 2: Data with Invalid Entries

## Input

[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

## Output

```
Invalid Entries Ignored: [-1, 0, -5]

Frequency Count:
1 → 1
2 → 2
3 → 3
4 → 1

Most Frequent: 3
Least Frequent: 1 or 4
```

---

# Scenario 3: Highly Skewed Data

## Input

[5, 5, 5, 5, 2, 2, 1]

## Output

```
Frequency Count:
1 → 1
2 → 2
5 → 4

Most Frequent: 5
Least Frequent: 1
```

---

# Scenario 4: All Same Values

## Input

[7, 7, 7, 7, 7]

## Output

```
Frequency Count:
7 → 5

Most Frequent: 7
Least Frequent: 7
```

---

# Scenario 5: Empty / Invalid Only Data

Input - [-1, 0, -3]

Output - No valid data found'''

#value and count from user
# n = int(input("Enter number of values: "))
# arr=[]
# for i in range(n):
#     x = int(input(f"value{i+1}: "))
#     arr.append(x)



# x = sorted(arr)
# unique_x = []
# for i in x:
#     if i not in unique_x:
#         unique_x.append(i)

# print(unique_x)

# max_count=0
# max=""
# least=""
# #least_count=99
# for i in unique_x:
#     count=0
#     for j in arr:
#         if j==i:
#             count+=1
#     print(i,"→",count)
#     if count>max_count:
#         max_count=count
#         max=i
#     else:
#         least_count=count
#         if count<=least_count:
#             least_count=count
#             least+=str(i)
# print(max,"\n",least)


# value and count from user
n = int(input("Enter number of values: "))

arr=[]

for i in range(n):
    x = int(input(f"value{i+1}: "))
    arr.append(x)

# remove invalid values
valid = []
invalid = []

for i in arr:
    if i > 0:
        valid.append(i)
    else:
        invalid.append(i)

# no valid data
if len(valid) == 0:
    print("No valid data found")

else:
    x = sorted(valid)
    unique_x = []

    for i in x:
        if i not in unique_x:
            unique_x.append(i)
    print("\nFrequency Count:")

    max_count = 0
    least_count = len(valid)
    max_values = []
    least_values = []

    # frequency checking
    for i in unique_x:
        count = 0
        for j in valid:
            if j == i:
                count += 1

        print(i, "→", count)

        # max
        if count > max_count:
            max_count = count

        # least
        if count < least_count:
            least_count = count

    for i in unique_x:

        count = 0

        for j in valid:
            if j == i:
                count += 1

        if count == max_count:
            max_values.append(i)

        if count == least_count:
            least_values.append(i)

    # invalid entries
    if len(invalid) > 0:
        print("\nInvalid Entries Ignored:", invalid)

    print("\nMost Frequent:", *max_values)
    print("Least Frequent:", *least_values)