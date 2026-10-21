'''7. Ride Booking Surge Pricing System

A ride booking app calculates fare multiplier based on demand, time, and distance.

If demand is at least 80, then check time. If peak time, then check distance. If distance is at least 10, apply 2x fare; otherwise 1.5x. If not peak time, then check if demand is at least 90. If yes, 1.8x; otherwise 1.3x. If demand is less than 80, then check if demand is at least 50. If yes, then if peak time, apply 1.2x; otherwise normal fare. If demand is below 50, normal fare.

Input:
Demand = 85
Time = peak
Distance = 12

Output:
Fare Multiplier = 2x Fare'''


demand = float(input("Demand = "))
time = input("Time = ").lower()
distance = float(input("Distance = "))

if demand>=80:
   if time=="peak":
       if distance>=10:
           print("Fare Multiplier = 2x Fare")
       else:
           print("Fare Multiplier = 1.5x Fare")

   else:
       if demand>=90:
           print("Fare Multiplier = 1.8x Fare")
       else:
           print("Fare Multiplier = 1.3x Fare")

elif demand>=50:
       if time=="peak":
           print("Fare Multiplier = 1.2x Fare")
       else:
           print("Fare Multiplier = Normal Fare")
else:
           print("Fare Multiplier = Normal Fare")


