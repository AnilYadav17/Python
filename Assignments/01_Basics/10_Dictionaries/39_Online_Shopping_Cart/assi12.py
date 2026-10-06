'''
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
'''

orders = [
    "Pizza",
    "Burger",
    "Pizza",
    "Pasta",
    "Burger",
    "Pizza",
    "Pasta"
]

order_count = {}
for item in orders:
    order_count[item] = order_count.get(item, 0) + 1

for item, count in order_count.items():
    print(f"{item} : {count}")

print()  # Print blank line to match sample output format

# Find the most ordered item
most_ordered = None
max_orders = 0

for item, count in order_count.items():
    if count > max_orders:
        max_orders = count
        most_ordered = item

print("Most Ordered :", most_ordered)
