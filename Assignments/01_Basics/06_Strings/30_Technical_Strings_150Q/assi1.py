'''1.
Find the length of a string.'''

s = input("Enter String to find its length: ")
count=0

for i in s:
    count+=1

print("Length(By Method):",len(s))
print("Length(Manualy):",count)