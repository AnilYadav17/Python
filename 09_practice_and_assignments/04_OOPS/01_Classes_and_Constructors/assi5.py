'''
Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0'''

class Guest:

    def __init__(self,id,name,number_of_days,charge):
        self.charge_per_day = charge
        self.id = id
        self.name = name
        self.number_of_days = number_of_days
        self.total()
        self.display()

    def total(self):
        self.room_bill = self.charge_per_day * self.number_of_days
        self.gst_price = self.room_bill * 12 / 100
        self.final_bill = self.room_bill + self.gst_price

    def display(self):
        print(f"""
------ Hotel Bill ------
Guest ID              : {self.id}
Guest Name            : {self.name}
Number of Days        : {self.number_of_days}
Room Charge Per Day   : ₹{self.charge_per_day}
Room Bill             : ₹{self.room_bill}
GST (12%)             : ₹{self.gst_price}
Final Bill            : ₹{self.final_bill}
""")

id = input("Enter Guest ID : ")
name = input("Enter Guest Name : ")
num = int(input("Enter Number of Days : "))
charge = int(input("Enter Room Charge Per Day : "))

g1 = Guest(id,name,num,charge)