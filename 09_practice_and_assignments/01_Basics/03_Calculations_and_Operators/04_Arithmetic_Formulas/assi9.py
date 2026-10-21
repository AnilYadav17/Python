'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0'''

distance,mileage,price =  map(float,input("Enter Distance,Mileage and Petrol Price :").split())
print("Petrol used :",distance/mileage,"litres")
print("Total cost :",distance/mileage*price)
