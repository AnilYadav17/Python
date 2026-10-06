'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500'''

distance,mileage,price = map(float,input("Enter distance (km), mileage (km/litre), and petrol price: ").split())
print("Cost :",round(distance/mileage*price,3))
