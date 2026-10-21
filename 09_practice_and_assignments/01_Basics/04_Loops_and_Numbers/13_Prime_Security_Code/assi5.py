'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''



num = int(input("Enter Number = "))
org=num
while True:
   num+=1
   flag = 0
   for i in range(2,num//2+1):
       if num%i==0:
         flag=1
         break
   if flag==0:
      next=num
      print(num)
      break
   num+=1

print("Difference",next-org)

