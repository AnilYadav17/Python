s1 = input("Enter string: ")
#words=set()
#for i in s1:
#	words.add(i)
#print(words)

print(s1)
print(set(s1))

if len(s1)==len(set(s1)):
	print("No Duplicates")
else:
	print("Duplicates are there")
