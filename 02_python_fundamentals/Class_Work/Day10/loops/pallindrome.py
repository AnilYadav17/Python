# n = int(input("Enter Number: "))
# rev = ""
# m=n= str(n)
# for i in n:
#     rev=i+rev
# if m==rev:
#     print("Palindrome")



n = int(input("Enter any Number:"))
rev=0
m=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

if rev==m:
    print("Pollindrome")
else:
    print("Not Pollindrome")
