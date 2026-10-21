'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4'''

seconds = int(input("Enter total seconds :"))
hrs = seconds//3600
x =  seconds%3600
mins = x//60
sec = x-mins*60
print("Hours :",hrs,"\nMinutes :",mins,"\nSeconds :",sec)


