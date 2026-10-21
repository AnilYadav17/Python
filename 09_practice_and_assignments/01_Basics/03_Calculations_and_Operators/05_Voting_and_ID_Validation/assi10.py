'''10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate'''

marks = int(input("Enter marks:"))
attendance = int(input("Enter attendance:"))
if marks>=40:
    print("Pass")
    if attendance>=75:
        print("Eligible for certificate")
