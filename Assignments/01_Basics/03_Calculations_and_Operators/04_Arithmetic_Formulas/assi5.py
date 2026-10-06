'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''

m_salary,w_days,w_hrs = map(float,input("Enter Monthly salary , Working days and Working hours per day: ").split())
salary_day = m_salary/w_days
salary_hr = salary_day/w_hrs
print("Salary per day:",salary_day,"\nSalary per hour:",salary_hr)
