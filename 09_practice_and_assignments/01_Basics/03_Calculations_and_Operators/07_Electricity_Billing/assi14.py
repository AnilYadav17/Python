'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

category = input("Enter course category (Programming,Design or Marketing) : ").lower()
user_type = input("Enter User Type (Student , WOkring or Others) :").lower()


if category=="programming":
    cost = 5000
    if user_type=="student":
        cost-=cost*20/100
        print("Final Course Fee: ₹",cost)
    elif user_type=="working":
        cost-=cost*10/100
        print("Final Course Fee: ₹",cost)
    else:
        print("Final Course Fee: ₹",cost)
elif category=="design":
    cost = 4000
    if user_type=="student":
        cost-=cost*20/100
        print("Final Course Fee: ₹",cost)
    elif user_type=="working":
        cost-=cost*10/100
        print("Final Course Fee: ₹",cost)
    else:
        print("Final Course Fee: ₹",cost)
elif category=="marketing":
    cost = 3000
    if user_type=="student":
        cost-=cost*20/100
        print("Final Course Fee: ₹",cost)
    elif user_type=="working":
        cost-=cost*10/100
        print("Final Course Fee: ₹",cost)
    else:
        print("Final Course Fee: ₹",cost)

else:
    print("No course available!")
