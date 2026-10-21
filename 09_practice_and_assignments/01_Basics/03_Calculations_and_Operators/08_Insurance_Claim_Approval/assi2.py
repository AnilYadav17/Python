'''2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted'''

marks = int(input("Marks = "))
score = int(input("Entrance Score = "))
category = input("Category = ").lower()


if marks>=70:
    if score>=80:
        if category=="general":
            print("Admission Status = Admitted")
        else:
            print("Admission Status = Admitted with Scholarship")
    else:
         if marks>=85:
             print("Admission Status = Admitted under Management Quota")
         else:
             print("Admission Status = Rejected")
else:
    if category!="general":
        if marks>=60:
            if score>=70:
                print("Admission Status = Waitlist")
            else:
                print("Admission Status = Rejected")
        else:
                print("Admission Status = Rejected")
    else:
                print("Admission Status = Rejected")
