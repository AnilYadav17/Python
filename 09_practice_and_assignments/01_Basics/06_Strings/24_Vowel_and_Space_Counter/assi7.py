'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''

# #manualy
# num = input("Enter vehicle number: ").lower()
# flag = False

# if len(num) == 10:
#     for ch in num[:2]:
#         if ch >= "a" and ch <= "z":
#             flag = True
#         else:
#             flag = False
#             break

#     if flag == True:
#         for ch in num[2:4]:
#             if ch >= "0" and ch <= "9":
#                 flag = True
#             else:
#                 flag = False
#                 break

# if flag == True:
#     print("Valid Vehicle Number")
# else:
#     print("Invalid Vehicle Number")



#using Methods
num = input("Enter vehicle number: ")
flag = False

if len(num) == 10:
    for ch in num[:2]:
        if ch.isalpha() == True:
            flag = True
        else:
            flag = False
            break
            
    # Only check digits if the alphabet check passed
    if flag == True:
        for ch in num[2:4]:
            if ch.isdigit() == True: 
                flag = True
            else:
                flag = False
                break

if flag == True:
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")