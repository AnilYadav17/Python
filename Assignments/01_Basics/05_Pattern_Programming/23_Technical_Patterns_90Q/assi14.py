'''14.
1
23
456
78910'''
count=1
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(count,end="")
        count+=1
    print()