a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter c:"))
d = int(input("Enter D:"))

if a>b:
	if a>c:
		if a>d:
			print("A is Greater")
		else:
			print("D is Greater")
	else:
		if c>d:
			print("C is Greater")
		else:
			print("d is Greater")
else:
	if b>c:
		if b>d:
			print("b is Greater")
		else:
			print("d is Greater")
	else:
		if c>d:
			print("c is Greater")
		else:
			print("d is Greater")
