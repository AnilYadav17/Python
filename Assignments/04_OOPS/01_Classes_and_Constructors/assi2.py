'''Question 2: Electricity Bill Calculator
Scenario

An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:
customer_id
customer_name
units_consumed

Initialize the values using a constructor.
Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350

Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Total Bill Amount : ₹2950.0'''


class Customer:
    # cost_per_charge=8
    # fixed_charge = 150

    def __init__(self,id,name,units):
        self.cost_per_charge=8
        self.fixed_charge = 150
        self.id=id
        self.name=name
        self.units=units
        self.total_amount()
        self.display()

    def total_amount(self):
        self.total = ( self.units * self.cost_per_charge ) + self.fixed_charge

    def display(self):
        print(f"""
------ Electricity Bill ------
Customer ID       : {self.id}
Customer Name     : {self.name}
Total Bill Amount : {self.total}
""")


id = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))


e1 = Customer(id,name,units)
