'''6. A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input. 
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening, 
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.

Input:
Age = 25
Show Time = evening
Day = weekend

Output:
Ticket Price = 300'''

age = int(input("Age = "))
show_time = input("Show Time (morning/evening) = ").lower()
day = input("Day (weekend/notWeekend) = ").lower()

if 18>age:
    if show_time=="morning":
        print("Ticket Price = 100")
    else:
        print("Ticket Price = 150")
else:
    if show_time=="evening":
        if day=="weekend":
            print("Ticket Price = 300")
        else:
            print("Ticket Price = 250")
    else:
        print("Ticket Price = 200")
