#Append :- We can not read in Append mode.
with open("demo.txt","a") as file:
    file.write("\nHii buddy")

with open("demo.txt") as file:
    data = file.read()
    print(data)

