'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked'''

cart_value = float(input("Enter cart value :"))
if cart_value>=500:
    print("Free delievery applied")
    if cart_value>=1200:
        print("Discount coupon unloacked")
