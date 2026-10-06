import calendar
print(calendar.calendar(2026))
#print(calendar.month(2027, 1))

#print(calendar.weekday(2026,06,02))
print(list(calendar.day_name)) 
print(list(calendar.month_name))

y = int(input("\nEnter year: "))
for i in range(1,13):
    print(calendar.month(y,i))
    
x = int(input("\nEnter year to check (leap year or not): "))
if calendar.isleap(x):
    print("Given year is leap year")
else:
    print("Giver year is not leap year")
    
    
x,y = map(int,input("\nEnter month and year using space: ").split())
print(calendar.monthrange(y,x))


#Set first day of Weak
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026,7))
