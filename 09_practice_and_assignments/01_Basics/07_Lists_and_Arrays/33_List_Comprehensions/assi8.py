'''8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found'''



n = int(input("Enter length of sequence: "))
arr1=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr1.append(x)
arr=arr1.copy()


#majority element
majority_count = n/2
majority_element=-1

for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>majority_count:
        majority_element=i
if majority_element!=-1:
    print(f"Majority element: {majority_element}")
else:
    print("No Majority element found")