'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''


vehicle_type = input("Enter Vehicle type: ").lower()
hrs_parked = int(input("Enter Hours parked: "))

if hrs_parked<=5:
   if vehicle_type=="bike":
       print("Total Parking Fee:",hrs_parked*10)
   elif vehicle_type=="car":
       print("Total Parking Fee:",hrs_parked*20)
   else:
       print("Total Parking Fee:",hrs_parked*50)
else:
   if vehicle_type=="bike":
       print("Total Parking Fee:",hrs_parked*10+100)
   elif vehicle_type=="car":
       print("Total Parking Fee:",hrs_parked*20+100)
   else:
       print("Total Parking Fee:",hrs_parked*50+100)
