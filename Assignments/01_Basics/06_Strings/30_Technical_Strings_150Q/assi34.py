'''34.Find the shortest word.'''

s = input("Enter string: ")
l = s.split()
short=99
result=""

for i in l:
    if short>len(i):
        short=len(i)
        result=i

print(f"{result} is smallest word with length {short}")