'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31'''

#num = int(input("Enter Number = "))
#flag = 0
#i=2
#for i in range (i,num//2+1):
#    if num%i==0:
#       flag=1
#       break
#if flag==0:
#   print("Prime Number")
#   num+=1
#   flag==0
#   while True:
#       for i in range(2,num//2+1):
#          if  num%i==0:
#            flag=1
#            break
#    if flag==0:
#          print("Next Prime =",num)
#           break
#       num+=1


num=int(input("Input:"))
x=0
if num<=1:
    print("Not prime")
i=2
while i<(num-1):
    if num%i==0:
        x=1
        break
    i=i+1
if x==1:
    print("not prime")
else:
    print("prime")
    
if x==0:
    
    i=num+1
    sum=0
    
    
    while True:
            j=2
            while j<=i//2:
                if i%j==0:
                    break
                j=j+1
            if j>i//2:
                print(i)
                break
            i=i+1
else:
    i=num-1
    sum=0
    
    
    while True:
            j=2
            while j<=i//2:
                if i%j==0:
                    break
                j=j+1
            if j>i//2:
                print(i)
                break
            i=i-1
