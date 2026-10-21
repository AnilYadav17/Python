'''
=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"ajay@gmail.com",
"ravi@yahoo.com",
"neha@gmail.com",
"aman@outlook.com",
"abc@gmail.com"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}
'''

emails = [
    "ajay@gmail.com",
    "ravi@yahoo.com",
    "neha@gmail.com",
    "aman@outlook.com",
    "abc@gmail.com"
]

domain_count = {}
for email in emails:
    domain = email.split('@')[1]
    domain_count[domain] = domain_count.get(domain, 0) + 1

print(domain_count)
