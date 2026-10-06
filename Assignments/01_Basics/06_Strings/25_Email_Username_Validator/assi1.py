"""1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username"""

username = input("Enter username: ").lower()
space = 0
flag = False
if len(username)>=5 and len(username)<=12 and username[0]>="a" and username[0]<="z":
    for ch in username:
        if ch!=" " or  (ch>="0" and ch<="9") or ch=="_":
            flag=True
        else:
            flag=False
            break
if flag==True:
    print("Valid Username")
else:
    print("Invalid Username")