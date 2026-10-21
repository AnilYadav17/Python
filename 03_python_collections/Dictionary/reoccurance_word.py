word = input("Enter word: ")
d={}

for i in word:
	d[i]=d.get(i,0)+1

print(d)
print()
for i,j in d.items():
	print(i,"Occured",j,"times.")
