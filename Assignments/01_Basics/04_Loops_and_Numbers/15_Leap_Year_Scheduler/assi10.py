'''10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill
---
Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''


n=int(input("Enter  the house no = "))
sum=0
maxbill=0
for i in range(1,n+1):
    units=int(input(f"Enter the units of {i} house "))
    if units<=100:
        bill=units*5
        #sum+=bill
        if units<50:
            bill=bill-100
        sum+=bill
    elif 101<units<=200:
        bill=(units-100)*7+(100*5)
        sum+=bill
    elif units>200:
        bill=(units-200)*10+100*5+100*7
        sum+=bill
    if bill>2000:
        bill=(20/100)*bill
    if bill>maxbill:
        maxbill=bill    
    print(bill)
print("THe total collecction = ",sum)
print("Highest bill = ",maxbill)
