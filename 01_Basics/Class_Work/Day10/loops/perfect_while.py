n = int(input("Enter the number = "))
sum = 0

while i<=n//2:
    if n%i==0:
        sum=sum+i
    i+=1
if sum==n:
    print("Pefect Number")
else:
    print("Not Perfect Number")