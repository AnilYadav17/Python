'''68.Count the sum of digits present in a string.'''

s = input("Enter string: ")
sum=0

for i in s:
    if i.isdigit()==True:
        sum+=int(i)

print("Sum:",sum)