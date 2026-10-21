'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''

#using method
# num = input("Enter Number: ")
# if len(num) == 12 and num[:3] == "PNR" and num[3:].isdigit():
#     print("Valid PNR Number")
# else:
#     print("InValid PNR Number")



#Manualy
num = input("Enter Number: ")
flag = False

if len(num) == 12 and num[:3] == "PNR":
    flag = True
    for ch in num[3:]:
        if not ("0" <= ch <= "9"):
            flag = False
            break

if flag == True:
    print("Valid PNR Number")
else:
    print("Invalid PNR Number")