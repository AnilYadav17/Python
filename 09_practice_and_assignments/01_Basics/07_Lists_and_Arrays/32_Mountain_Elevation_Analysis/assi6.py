'''6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0'''


n = int(input("Enter size of values: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Energy value: "))
    arr.append(x)

#copy
arr1= arr.copy()

#prime ids
primes=[]
sum=0
count=0
for i in arr1:
    f=True
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                f=False
                break
        if f:
            primes.append(i)
            sum+=i
            count+=1



if primes!=[]:
    #max
    max=primes[0]
    for i in primes:
        if i>max:
            max=i

    #print        
    print(f"""Prime IDs = {primes}
Sum = {sum}
Max = {max}
Count = {count}""")
else:
    print('''Prime IDs = []
Sum = 0
Max = -1
Count = 0''')