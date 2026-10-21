'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction'''


marks = int(input("Enter Marks :"))
if marks>=40:
    print("Pass")
    if marks>=75:
        print("Distinction")
