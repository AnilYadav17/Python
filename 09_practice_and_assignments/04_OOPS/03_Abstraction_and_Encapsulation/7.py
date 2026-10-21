# Problem 2: Pizza Ordering System

class Pizza:
    def __init__(self, base_price, topping_cost):
        self.base_price = base_price
        self.topping_cost = topping_cost
        
    def calculatePrice(self, toppings):
        return self.base_price + (self.topping_cost * toppings)

class DiscountedPizza(Pizza):
    def calculatePrice(self, toppings):
        regular_price = super().calculatePrice(toppings)
        if toppings > 3:
            return regular_price * 0.9
        return regular_price

if __name__ == "__main__":
    base = float(input())
    topping_cost = float(input())
    toppings = int(input())
    
    pizza = Pizza(base, topping_cost)
    regular = pizza.calculatePrice(toppings)
    
    discounted_pizza = DiscountedPizza(base, topping_cost)
    discounted = discounted_pizza.calculatePrice(toppings)
    
    print(f"Price without discount: Rs.{regular:.2f}")
    print(f"Price with discount: Rs.{discounted:.2f}")
