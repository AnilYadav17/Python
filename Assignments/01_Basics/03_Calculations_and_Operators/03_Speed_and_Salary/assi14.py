'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''

cost_price,selling_price= map(float,input("Enter Cost Price and Selling Price (use comma to separate) :").split(","))
if(cost_price>selling_price):
 loss = cost_price-selling_price
 print("Loss\t:",loss)
 print("Loss%\t:",(loss/cost_price)*100)
elif cost_price<selling_price:
 profit = selling_price - cost_price
 print("Profit\t:",profit)
 print("Profit%\t:",(profit/cost_price)*100)
else:
 print("No Profit , No Loss")
