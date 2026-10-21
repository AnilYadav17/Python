id = input("Enter Transaction ID = ")
org = int(id)
reverse = ""
difference = 0
for i in id:
	reverse = i+reverse
print("Reverse = ",reverse)

reverse=int(reverse)
if org>reverse:
	difference=org-reverse
else:
	difference=reverse-org
print("Difference = ",difference)
print("Digits = ",len(str(difference)))

if difference==0:
	print("Perfect Match")
elif difference%9==0:
	print("Verified")
else:
	print("Rejected")
