'''21.Find the first non-repeating character.'''


s = input("Enter String: ")
max=0

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count==1:
        print("First non repeating character: ",i)
        break
else:
    print("No non repeating character found")