def counts(n):
	if  n ==0:
		return 0
	return 1+counts(n//10)

n = int(input("Enter number to count digit: "))
print(counts(n))
