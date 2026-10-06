'''Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0'''



class Product:

    def __init__(self,id,name,quantity,price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_amount()
        self.display()

    def total_amount(self):
        self.total = self.quantity * self.price 
        if self.total > 5000:
            self.discount_price = self.total / 10
        else:
            self.discount_price = self.total / 20
        self.final_amount = self.total - self.discount_price

    def display(self):
        print(f"""
------ Shopping Bill ------
Product ID        : {self.id}
Product Name      : {self.name}
Quantity          : {self.quantity}
Price Per Item    : {self.price}
Total Amount      : {self.total}
Discount          : {self.discount_price}
Final Amount      : {self.final_amount}
""")


id = input("Enter Product ID: ")
name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price Per Item: "))


p1 = Product(id,name,quantity,price)
