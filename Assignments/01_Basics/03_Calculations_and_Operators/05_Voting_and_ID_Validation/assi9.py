'''9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''

is_active = input("Membership active (yes/no):")

if is_active=="yes":
    print("Entry allowed")
    books_issued = int(input("Book issued:"))

    if books_issued<3:
        print("Can issue more books")
