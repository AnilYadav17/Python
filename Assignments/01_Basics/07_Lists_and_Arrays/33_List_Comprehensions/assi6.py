'''====================================================================
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]'''

#Taking input from user
n = int(input("Enter length of numbers: "))
arr=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr.append(x)

products=[]
for i in range(len(arr)):
    product=1
    for j in range(len(arr)):
        if i!=j:
            product*=arr[j]
    products.append(product)

print(products)