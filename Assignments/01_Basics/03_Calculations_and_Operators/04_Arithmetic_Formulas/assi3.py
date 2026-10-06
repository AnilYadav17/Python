'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2'''

m1,m2,m3,m4,m5 = map(float,input("Enter marks of 5 subjects: ").split(","))
total = m1+m2+m3+m4+m5
average = total/5
percent = total/500*100
print("Total:",total,"\nAverage:",average,"\nPercentage:",percent)
