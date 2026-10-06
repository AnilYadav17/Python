'''31.Remove duplicate words.'''

s = input("Enter string: ")
l = s.split()
result=""

for i in l:
    if i not in result:
        result+=i+" "

print("Resut:",result)