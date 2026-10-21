#WAP to  group words by length.

words  = ["Anii","Anil", "Virat","Yadav","Kohli","a","b"]

result = {}

for i in words:
	l=len(i)
	if l not in result:
		result[l]=[]
	result[l].append(i)

print(result)
