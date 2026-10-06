'''30. Replace a word with another word.'''

s = input("Enter string (to update): ")
ch = input("Enter target: ")
ch1 = input("Enter update: ")
l = s.split()
result=""
count=0

for i in l:
    if ch==i:
        result+=ch1+" "
    else:
        result+=i+" "

print("Updated string:",result)