'''5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website'''

website = input("Enter website: ")

lst1 = website.split(".")
if lst1[0]=="www" and lst1[2]=="com":
    print("Valid Website")
else:
    print("Invalid Website!")