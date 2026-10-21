'''=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple
O = namedtuple("Orders",["order_id","customer_name","product_name","amount"])

n = int(input("Enter Number of Orders: "))
orders=[]
for i in range(n):
    print(f"\nEnter Order{i+1} details: ")
    id=input("Enter Order ID: ")
    o_name=input("Enter Order name: ")
    p_name=input("Enter product name: ")
    a=float(input("Enter product amount: "))
    orders.append(O(id,o_name,p_name,a))

print("\n All Order Details: ")
for i in range(n):
    print(*orders[i])

highest=orders[0]
for i in range(n):
    if orders[i].amount>highest.amount:
        highest=orders[i]
print("\nHighest Value Order:\n",*highest)

count=0
total=0
for i in range(n):
    total+=orders[i].amount
    if orders[i].amount>10000:
        count+=1
print("\nTotal Sales:\n",total)
print("\nOrders Above ₹10,000:\n",count)