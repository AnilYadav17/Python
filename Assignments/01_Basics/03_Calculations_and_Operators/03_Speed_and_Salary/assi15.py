'''Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''

d1,t1 = map(float,input("Enter the Distance1,Time1 (Separate using comma): ").split(","))
d2,t2 = map(float,input("Enter the Distance2,Time2 (Separate using comma): ").split(","))
print("Average Speed: ",((d1+d2)/(t1+t2)),"km/h")
