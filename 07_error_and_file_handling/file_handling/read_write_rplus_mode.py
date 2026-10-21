#It opens file for both reading and writing  and file must be exist.
with open("demo1.txt","r+") as file:
    data = file.read()
    print(data)
    file.write("\n")
    data = file.read()
    print(data)