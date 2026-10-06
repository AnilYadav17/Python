'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password'''


username = input("Enter Username :")
password = input("Enter Password :")

if username=="admin":
    print("Valid user")
if len(password)>=8:
    print("Strong password")
