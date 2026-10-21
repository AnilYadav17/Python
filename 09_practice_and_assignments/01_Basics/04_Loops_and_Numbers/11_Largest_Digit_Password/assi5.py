'''5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6'''


n = int(input("Enter any Number = "))
count,i=0,1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
print("Factors Count = ",count)