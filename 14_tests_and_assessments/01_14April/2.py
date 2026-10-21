'''n = int(input("Enter Number = "))
diff = 0
greater = 0
smaller = 9
while n>0:
	digit = n%10
	if digit>greater:
		greater=digit
		diff = greater 
	elif digit<smaller:
		smaller = digit
	print(diff)
	n= n//10'''

'''m = str(n)
x= 9
for i in m:
	i= int(i)
	diff = x-i
	x = i
	if diff==0:
		pass
	else:
		print(diff)
x = 0
while n>0:
	digit =  n%10
	x = digit
	while n>0:
		digit=n%10
		diff = digit-x
		print(digit)
		n= n//10
	n= n//10'''


n = int(input("Enter Number = "))
diff = 0
greater = 0
smaller = 9
m = str(n)
sum = 0
x=0
new_diff = ""
#for i in m:
#	diff = int(i)-x
#	print(abs(diff))
#a = 0 
#for i in m:
#	n= int(i)
#	digit = n%10
#	a=digit
#	n= n//10
#	print(a)


#while n>0:
#       digit = n%10
#       if digit>greater:
#               greater=digit
#               diff = greater 
#       elif digit<smaller:
#               smaller = digit
#       print(diff)
#        n= n//10

for i in m:
	if diff==0:
		diff=int(i)
	else:
		diff= diff-int(i)
		print(abs(diff))
		sum += abs(int(diff))
		#new_diff = new_diff+" "+str(abs(diff))
		new_diff = new_diff+str(abs(diff))
		diff= int(i)
print("Step Diff = ",new_diff)
print("Sum = ",sum)
new_diff = int(new_diff)
largest=0

while new_diff>0:
	digit = new_diff%10
	if digit>largest:
		largest=digit
	new_diff= new_diff//10
print("Largest = ",largest)
length = len(str(n))

if sum%length==0:
	print("Balanced")
else:
	print("Unbalanced Number")

