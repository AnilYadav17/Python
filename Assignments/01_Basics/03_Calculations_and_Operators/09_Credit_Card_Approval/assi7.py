'''7. University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction'''


marks = int(input("Marks = "))
backlog = int(input("Backlogs = "))
project = int(input("Project = "))


if marks>=75:
   if backlog==0:
     if project>=80:
       print("Result = First Class with Distinction")
     else:
       print("Result = First Class ")
   else:
       print("Result = First Class ")
elif marks>=60:
   if backlog<=2:
       print("Result = Second Class")
   else:
       print("Result = Pass Class")
else:
   if marks>=50:
      print("Result = Pass")
   else:
      print("Result = Fail")
