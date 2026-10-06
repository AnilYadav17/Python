'''5.Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.'''

#test case
year = int(input("Enter Year = "))
print("Leap Year") if year%400==0 or year%4==0 else print("Not Leap Year")

# Real Logic
# result = "Leap Year" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "Not a Leap Year"
# print(result)