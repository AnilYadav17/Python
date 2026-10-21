'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''

initial = float(input("Enter bill amount: "))
final = 0
if initial>1000:
    if initial<5000:
        initial += initial*12/100
        print("Final Bill Amount: ₹",initial)
    else:
        initial +=initial*20/100
        print("Final Bill Amount: ₹",initial)
else:
    initial += initial*5/100
    print("Final Bill Amount: ₹",initial)
