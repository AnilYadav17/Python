'''35.Find the first palindrome word.'''

s = input("Enter string: ")
l = s.split()

for i in l:
    if i==i[::-1]:
        print("First polindrome in string:",i)
        break