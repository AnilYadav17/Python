#Exclusive creation mode , it creates a new file only
#If file  already exists then it gives error.
#We can not read in this mode.
with open("demo1.txt","x") as file:
    file.write("\nHii buddy")