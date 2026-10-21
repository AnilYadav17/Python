#WAP to find number of occurance vowel in string


s = input("Enter string: ")
v = set("aeiou")
d = {}

for i in s:
	if i in v:
		d[i]= d.get(i,0)+1
print(d)
print()

for i,j in sorted(d.items()):
	print(f"{i} Occured {j} times")
