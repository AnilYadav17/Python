'''7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable'''


salary =  float(input("Enter salary:"))
if salary>=30000:
    print("PF applicable")
    if salary>=50000:
        print("Bonus applicable")
