'''====================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6'''

print("""====================
ONLINE SHOPPING CART
====================""")
d = {}

n = int(input("Enter number of Items: "))
for i in range(n):
    name = input("Enter name of product: ")
    value = int(input("Enter Quantity: "))
    d[name]=value

sum=0
for quantity in d.values():
    sum+=quantity

print(f"The total quantity of products purchased is {sum}")
