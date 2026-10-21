#WAP to track how many times each user tried to login from the list.

#n = int(input("Enter number of Users: "))


logins = ["Anil", "Anu", "Anii", "Anil", "abc"]
d = {}

for user in logins:
	d[user] = d.get(user,0)+1

for i,j in d.items():
	print(f"{i} logined {j} times.")
