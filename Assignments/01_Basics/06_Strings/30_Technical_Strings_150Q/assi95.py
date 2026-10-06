'''95. Find the second most frequent character.'''
#input : S = "aabbccdde"  ,->   c' or 'd'  
s = input("Enter string: ")

first = 0
second = 0

for i in s:

    count = s.count(i)

    if count > first:
        second = first
        first = count

    elif count > second and count != first:
        second = count

for i in s:
    if s.count(i) == second:
        print("Second Most Frequent Character =", i)
        break