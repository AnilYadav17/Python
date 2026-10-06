'''61.Count total alphabets, digits, and special characters.'''
 
s = input("Enter string: ")
alphabets=0
digits=0
special=0

for i in s:
    if i.isalpha()==True:
        alphabets+=1
    elif i.isdigit()==True:
        digits+=1
    elif i==" ":
        pass
    else:
        special+=1

print(f"Alphabets:{alphabets}, Digits:{digits}, Special Characters:{special}")