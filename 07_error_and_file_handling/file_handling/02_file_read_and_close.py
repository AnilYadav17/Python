#READ
file = open("demo.txt")
data  = file.read()
print(data)
file.close()                                          

#WRITE
file = open("demo.txt", "w")
data = input("Enter data :")
file.write(data)
file.close()                        

#READ
print("\nData In File: ")
file = open("demo.txt")
data  = file.read()
print(data)
file.close()  