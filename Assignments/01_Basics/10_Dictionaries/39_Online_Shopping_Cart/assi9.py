'''
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
'''

stock = {
    "Pen": 50,
    "Pencil": 100,
    "Eraser": 25,
    "Marker": 10
}

for product, quantity in stock.items():
    if quantity < 30:
        print(product)
