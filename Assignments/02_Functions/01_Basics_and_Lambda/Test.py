def display(name,*args):
	print(name,"is positional argument")
	for i in args:
		print(i,"is variable length argument")

display("Anil",1,2,3,4)
