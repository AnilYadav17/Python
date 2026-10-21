'''problem 3:  3 marks
==========


Rithish is developing a straightforward pizza ordering system. To achieve this, he needs a Pizza class with a constructor for
 the base price and topping cost, along with a calculatePrice method overriding. He also wants a DiscountedPizza class that inherits from
Pizza, applying a 10% discount for more than three toppings.

The program prompts the user for inputs, creates instances of both classes, calculates regular and discounted prices,
and displays them formatted appropriately.

Example 1

Input:
9.5
1.25
3
Output:
Price without discount: Rs.13.25
Price with discount: Rs.13.25
Explanation:
Rithish orders a pizza with a base price of Rs. 9.5, a topping cost of Rs. 1.25, and selects 3 toppings. The price is calculated as 9.5 + (1.25 * 3) = 13.25. The regular and discounted prices are both Rs. 13.25, as no discount has been applied.

Example 2

Input:
11.0
2.0
7
Output:
Price without discount: Rs.25.00
Price with discount: Rs.22.50
Explanation:
Rithish orders another pizza with a higher base price of Rs. 11.0, a topping cost of Rs. 2.0, and chooses 7 toppings.
Regular Price: 11.0 + (2.0 * 7) = Rs. 25.00.
Discounted Price: The discounted price is calculated as 90% of the regular price, i.e., 0.9 * 25.00 = Rs.22.50.
Input format :
The first line of input consists of a double value, representing the base price of the pizza.
The second line consists of a double value, representing the cost per topping.
The third line consists of an integer, representing the number of toppings chosen for the pizza.
Output format :
The first line of output prints the price without discount, rounded off to two decimal places.
The second line prints the price with the discount, rounded off to two decimal places.

Refer to the sample output for formatting specifications.
Code constraints :
The base price and the cost per topping should be greater than zero.
1 ≤ number of toppings ≤ 10
Sample test cases :
Input 1 :
9.5
1.25
3
Output 1 :
Price without discount: Rs.13.25
Price with discount: Rs.13.25
Input 2 :
11.0
2.0
7
Output 2 :
Price without discount: Rs.25.00
Price with discount: Rs.25.0'''


class Pizza:
    def __init__(self, base_price, topping_price, toppings):
        self.base_price = base_price
        self.topping_price = topping_price
        self.toppings = toppings
    
    def calculatePrice(self):
        return self.base_price + (self.topping_price * self.toppings)

class DiscountedPizza(Pizza):  
    def calculatePrice(self):
        regular_price = super().calculatePrice()
        if self.toppings > 3:
            return regular_price * 0.9
        return abs(regular_price,2)

base_price = float(input("Enter Base Price: "))
topping_price = float(input("Enter Topping Price: "))
toppings = int(input("Enter number of Toppings: "))

regular_pizza = Pizza(base_price, topping_price, toppings)
discounted_pizza = DiscountedPizza(base_price, topping_price, toppings)

print(f"Price without discount: Rs. {regular_pizza.calculatePrice(): }")
print(f"Price with discount: Rs.{discounted_pizza.calculatePrice(): }")

