# a = [1,2,3,4]
# k = 5
n = int(input("Enter length of array: "))
a=list(map(int,input('enter elements using "," :').split(",",maxsplit=n)))
k = int(input("Enter target: "))
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]+a[i]==k:
            count+=1
print(a)
print(count)