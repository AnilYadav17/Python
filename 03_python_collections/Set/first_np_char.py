s = input("Enter string: ")
#w = set(s)

seen=set()
rep=set()

for char in s:
	if char not in seen:
		rep.add(char)
		print(char)
		print(rep)
	seen.add(char)
	print(seen)


for char in s:
	if char not in  rep:
		print(f"First non-repeating char: {char}")
		break
else:
	print("No non-repeating character")
