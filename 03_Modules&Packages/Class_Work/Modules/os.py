import os
cwd = os.getcwd()


print("Current Working Directory is:",cwd)
os.mkdir("Hiii")
print("Hiii Created")
print(os.listdir())
os.rmdir("Hiii")
print("Hiii Deleted")
print(os.listdir())


print(os.getcwd())
os.chdir("..")
print(os.getcwd())
