'''22.Find the last repeating character.'''


s = input("Enter String: ")


for i in range(len(s)-1, -1,-1):
    count=0
    for j in range(len(s)-1, -1,-1):
        if s[i]==s[j]:
            count+=1
    if count==1:
        print("last non repeating character: ",s[i])
        break
else:
    print("No non repeating character found")