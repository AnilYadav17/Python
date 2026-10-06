'''=====================================================================
QUESTION 6: PRODUCT INFORMATION
==============================

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''

n = int(input("Enter number of products: "))
products = []
for i in range(n):
    print(f"\nEnter Product {i+1} details:")
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    price = int(input("Enter Price: "))
    products.append((product_id, product_name, price))

print("\nAll Products:")
for p in products:
    print(p)

costliest = products[0]
cheapest = products[0]
total_price = 0
for p in products:
    if p[2] > costliest[2]:
        costliest = p
    if p[2] < cheapest[2]:
        cheapest = p
    total_price += p[2]

print("\nCostliest Product:")
print(costliest)

print("\nCheapest Product:")
print(cheapest)

print("\nAverage Price:")
print(total_price / n)

print("\nProducts Above ₹50,000:")
for p in products:
    if p[2] > 50000:
        print(p)
