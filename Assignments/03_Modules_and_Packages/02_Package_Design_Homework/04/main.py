from Packages import for_add_customer, for_add_product, for_invoice, for_total, for_profile

add_customer = for_add_customer.add_customer
add_product = for_add_product.add_product
invoice = for_invoice.invoice
total = for_total.total
profile = for_profile.profile

while True:
    print("""
=============================
   ONLINE SHOPPING SYSTEM
=============================
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit
""")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("Enter customer details: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            mobile = int(input("Enter M.No: "))
            add_customer(name,email,mobile)
            
        case 2:
            name = input("Enter Product Name : ")
            price = int(input("Enter Price : "))
            cat = input("Enter Category : ")
            add_product(name=name,cat=cat,price=price)
            
        case 3:
            name = input("Enter Product name : ")
            price = int(input("Enter Product price : "))
            print("Total price with 10% Tax:",invoice(name,price))
            
        case 4:
            prices=[]
            n = int(input("Enter number of Pruducts: "))
            for i in range(n):
                prices.append(int(input(f"Enter Product{i+1} Price: ")))
            print("Total :",total(*prices))
            
        case 5:
            print("Enter customer details : ")
            name = input("Enter Name: ")
            city = input("Enter City: ")
            email = input("Enter Email: ")
            mobile = input("Enter M.NO: ")
            profile(name,city=city,email=email,mobile=mobile)
            
        case 6:
            print("Thanks for visiting , Online Shopping System ...")
            break
            
        case _:
            print("Invalid choice!")
