'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''

speed,hrs,min =  map(float,input("Enter Speed, Time in hour and min: ").split())
total_hrs = hrs+min/60
distance = total_hrs*speed
print("Total Time :",total_hrs,"hours")
print("Distance :",distance,"km")
