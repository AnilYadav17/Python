'''70. Compare the number of times 'the' and 'is' appear.'''

s = input("Enter string: ")
l = s.split()
is_count=0
the_count=0

for i in l:
    if i=="is":
        is_count+=1
    elif i=="the":
        the_count+=1

print(f"the:{the_count} ,is:{is_count}")
