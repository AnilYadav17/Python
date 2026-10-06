'''
=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''

sales = [
    "Mobile",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile"
]

sales_count = {}
for product in sales:
    sales_count[product] = sales_count.get(product, 0) + 1

# Display products sorted by product name (keys)
for product in sorted(sales_count.keys()):
    print(f"{product} : {sales_count[product]}")
