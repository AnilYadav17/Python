'''5. Smart Exam Evaluation System

A student’s result depends on marks, attendance, and internal score.

If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.

If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

Input:
Marks = 38
Attendance = 80
Internal = 26

Output:
Result = Reappear'''



marks = int(input("Marks = "))
attendance = int(input("Attendance = "))
internal = int(input("Internal = "))

if marks>=40:
   if attendance>=75:
      if internal>=20:
        print("Result = Pass")
      else:
        print("Result = Grace Pass")
   else:
        print("Result =  Detained")
else:
  if marks>=35:
    if internal>=25:
       print("Result = Reapper")
    else:
        print("Result = Fail")

