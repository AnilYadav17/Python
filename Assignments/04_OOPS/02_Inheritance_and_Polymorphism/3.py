# ASSIGNMENT 3: Online Shopping System (Hierarchical Inheritance)

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print(f"Product ID : {self.product_id}")
        print(f"Product Name : {self.product_name}")

class Electronics(Product):
    def __init__(self, product_id, product_name, price, brand, warranty):
        super().__init__(product_id, product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        print("Electronics Product\n")
        super().display()
        print(f"Brand : {self.brand}")
        print(f"Warranty : {self.warranty}")
        print(f"Price : ₹{int(self.price)}")

class Clothing(Product):
    def __init__(self, product_id, product_name, price, size, fabric_type):
        super().__init__(product_id, product_name, price)
        self.size = size
        self.fabric_type = fabric_type

    def display(self):
        print("Clothing Product\n")
        super().display()
        print(f"Size : {self.size}")
        print(f"Fabric Type : {self.fabric_type}")
        print(f"Price : ₹{int(self.price)}")

class Grocery(Product):
    def __init__(self, product_id, product_name, price, expiry_date, weight):
        super().__init__(product_id, product_name, price)
        self.expiry_date = expiry_date
        self.weight = weight

    def display(self):
        print("Grocery Product\n")
        super().display()
        print(f"Expiry Date : {self.expiry_date}")
        print(f"Weight : {self.weight}")
        print(f"Price : ₹{int(self.price)}")

if __name__ == "__main__":
    products = []
    while True:
        print("\n========== Online Shopping ==========")
        print("1. Add Electronics Product")
        print("2. Add Clothing Product")
        print("3. Add Grocery Product")
        print("4. Display Electronics")
        print("5. Display Clothing")
        print("6. Display Grocery")
        print("7. Exit")
        
        choice = input("Choice : ")
        
        if choice == '1':
            p_id = input("\nProduct ID : ")
            name = input("Product Name : ")
            price = float(input("Price : "))
            brand = input("\nBrand : ")
            warranty = input("Warranty : ")
            prod = Electronics(p_id, name, price, brand, warranty)
            products.append(prod)
            print()
            prod.display()
        elif choice == '2':
            p_id = input("\nProduct ID : ")
            name = input("Product Name : ")
            price = float(input("Price : "))
            size = input("\nSize : ")
            fabric = input("Fabric Type : ")
            prod = Clothing(p_id, name, price, size, fabric)
            products.append(prod)
            print()
            prod.display()
        elif choice == '3':
            p_id = input("\nProduct ID : ")
            name = input("Product Name : ")
            price = float(input("Price : "))
            expiry = input("\nExpiry Date : ")
            weight = input("Weight : ")
            prod = Grocery(p_id, name, price, expiry, weight)
            products.append(prod)
            print()
            prod.display()
        elif choice == '4':
            print()
            for p in products:
                if isinstance(p, Electronics):
                    p.display()
        elif choice == '5':
            print()
            for p in products:
                if isinstance(p, Clothing):
                    p.display()
        elif choice == '6':
            print()
            for p in products:
                if isinstance(p, Grocery):
                    p.display()
        elif choice == '7':
            break
