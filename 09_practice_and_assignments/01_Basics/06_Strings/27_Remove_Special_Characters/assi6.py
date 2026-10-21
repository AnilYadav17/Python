'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence: iphone is good and iphone battery is strong

Word: iphone

Output: 2'''

s1 = input("Enter Sentence:").lower()
target = input("Enter Word: ").lower()
count=0

# l1 = s1.split()
# for i in l1:
    # if i==target:
        # count+=1
# 
# print(f"{target} comes {count} times in Sentence")


for i in range(len(s1)-len(target)+1):
    match=1
    for j in range(len(target)):
        if s1[i+j]!=target[j]:
            match=0
            break
    if match==1:
        count+=1
print(f"{target} comes {count} times in Sentence")


