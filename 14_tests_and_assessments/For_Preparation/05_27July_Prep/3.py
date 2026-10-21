'''----------------------------------------------------------------------
Question 3: Object-Oriented Programming (Ride-Sharing System)
----------------------------------------------------------------------
A new cab booking startup wants to manage its daily rides using objects. 

Write a Python program to:
1. Create a class named `Ride` with the following attributes:
   - ride_id (string)
   - customer_name (string)
   - distance_km (float)
   - cab_type (string - can only be "Mini", "Sedan", or "SUV")

2. Create an `__init__` constructor to initialize these attributes.

3. Create a method `calculate_fare()` that calculates and returns the fare:
   - Base Fare: Mini = ₹50, Sedan = ₹80, SUV = ₹120
   - Per KM Charge: Mini = ₹10/km, Sedan = ₹15/km, SUV = ₹25/km
   - Formula: Total Fare = Base Fare + (Per KM Charge * distance_km)

4. Create a method `display_ride()` that prints the ride ID, customer name, 
   cab type, distance, and the total calculated fare.

5. Outside the class:
   - Create a list of 3 different Ride objects.
   - Loop through the list to display the details of all rides.
   - Find and print the name of the customer who paid the highest fare.

Example Objects:
ride1 = Ride("R01", "Anil", 12.5, "Sedan")
ride2 = Ride("R02", "Rahul", 5.0, "Mini")
ride3 = Ride("R03", "Priya", 20.0, "SUV")'''


class Ride:
    def __init__( self,ride_id, customer_name, distance_km, cab_type):
        self.ride_id = ride_id
        self.customer_name = customer_name
        self.distance_km = distance_km
        self.cab_type = cab_type
        
        
    def calculate_fare(self):
        if self.cab_type == "Mini":
            self.b_f = 50
            self.per_km = 10
        elif self.cab_type == "Sedan":
            self.b_f = 80
            self.per_km = 15
        else:
            self.b_f = 120
            self.per_km = 25
            
        self.Total_fare = self.b_f + (self.per_km * self.distance_km)
        return self.Total_fare    
        
    def display_ride(self):
        self.calculate_fare()
        return self.ride_id,self.customer_name,self.cab_type,self.distance_km,self.Total_fare
        

ride1 = Ride("R01", "Anil", 12.5, "Sedan")
ride2 = Ride("R02", "Rahul", 5.0, "Mini")
ride3 = Ride("R03", "Priya", 20.0, "SUV")
print(ride1.display_ride())
print(ride2.display_ride())
print(ride3.display_ride())
        
        
