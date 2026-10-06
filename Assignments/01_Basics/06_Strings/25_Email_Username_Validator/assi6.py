'''6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching'''


s1 = input("Enter first product code:").lower()
s2 = input("Enter second product code:").lower()
count1=0
count2=0
f=1

for ch in s1:
    if ch>="a" and ch<="z":
        count1+=1

for ch in s2:
    if ch>="a" and ch<="z":
        count2+=1

for ch in s1:
    if ch!=" ":
        if s1.count(ch)!=s2.count(ch):
            f=0
            break
if count1==count2 and f==1 :
    print("Both Product Codes are Matching")
else:
    print("Both Product Codes are not Matching")