'''
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System. The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.'''

customer=[]
product=[] 
profiles=[]

def add_customer(name,email,mobile):
    customer.append({
    "name":name,
    "email":email,
    "mobile":mobile
    })
    print("Customer Registered Successfully")
    

def add_product(name,price,cat):
    product.append({
    "name":name,
    "price":price,
    "category":cat
    })
    print("Product Details Displayed Successfully")
    
def invoice(name,price,tax=10):
    print("\n\tInvoice\nProduct Name:",name)
    print("Product Price:",price)
    return price+price*tax/100
    
def total(*args):
    return sum( args)
    
def profile(name,**args):
    profiles.append({
    "name":name,
    "city":city,
    "email":email,
    "mobile":mobile
    })
    print("Details updated...")
    for k in range(len(profiles)):
        for i,j in profiles[k].items():
            print(i,"\t",j)
    
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
            
