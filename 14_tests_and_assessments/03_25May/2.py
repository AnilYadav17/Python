'''2.
A graphics rendering engine displays signal strength in a diamond-shaped visualiz>

Write a Python program to print a star diamond pattern.

Input
Enter number of rows: 5



    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''



'''n = int(input("Enter number: "))

for i in range(n):
	for space in range(n-i-1,0,-1):
		print(" ",end="")
	for star in range(i*2+1):
		print("*",end="")
	print()

for i in range(n-2,-1,-1):
	for space in range((n-i)-1):
		print(" ",end="")
	for star in range((i)*2+1,0,-1):
                print("*",end="")
	print()'''




n = int(input("Enter Number:"))
for i in range(1,n+1):
        for space in range(n-i):
                print(" ",end="")
        for star in range(i*2-1):
                print("*",end="" )
        print()

for i in range(1,n):
        for space in range(i):
                print(" ",end="")
        for star in range((n-i)*2-2,-1,-1):
                print("*",end="" )
        print()


