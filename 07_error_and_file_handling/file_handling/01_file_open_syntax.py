'''
Synax -> file=open("filepath","mode")
default mode -> Read
'''
file=open("demo.txt","r")
print("Name:",file.name)
print("Mode:",file.mode)
print("Is Closed?:",file.closed)
file.close()
print("Is Closed?:",file.closed)


