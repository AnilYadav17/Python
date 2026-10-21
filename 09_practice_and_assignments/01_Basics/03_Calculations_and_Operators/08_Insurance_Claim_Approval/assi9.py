'''
9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike'''


experience = int(input("Experience = "))
rating = int(input("Rating = "))
projects = int(input("Projects = "))

if experience>=5:
   if rating>=4:
       if projects>=3:
          salary = float(input("Enter Salary = "))
          if salary>=50000:
             print("Promotion Status = Promoted with 30% hike")
          else:
             print("Promotion Status = Promoted with 20% hike")
       else:
             print("Promotion Status = Promoted with 10% hike")
   else:
       print("Promotion Status = No Promotion")
else:
    if rating==5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")


