'''5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password'''

password = input("Enter password: ")
digits = 0
special = 0
spaces = 0

if password[0]>="A" and password[0]<="Z":
    for ch in password:
        if ch>="0" and ch<="9":
            digits+=1
        elif ch.isalnum()==False and ch!=" ":
            special+=1
        elif ch==" ":
            spaces=1

if len(password)>=8 and len(password)<=15 and password[-1]>="0" and password[-1]<="9" and spaces==0 and digits>=2 and special>=1:
    print("Secure Password")
else:
    print("Insecure Password")