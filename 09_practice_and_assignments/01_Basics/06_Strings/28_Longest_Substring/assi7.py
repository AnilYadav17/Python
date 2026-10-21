'''7.
Customer Feedback Analysis System

An e-commerce company receives thousands of customer reviews every day for its products.

To analyze customer opinions efficiently, the analytics team wants a Python program that counts how many times each word appears in a review message.

This helps the company identify frequently used words such as:

good
bad
delivery
quality
service

Write a Python program to count the frequency of every word in a given sentence.

Input:
delivery was fast and delivery service was good
Output:
delivery : 2
was : 2
fast : 1
and : 1
service : 1
good : 1'''


s = input("Enter String: ")
l = s.split()
result=""


for i in l:
    count=0
    for j in l:
        if i == j:
            count+=1
    
    if i not in result:
        result += i + " "
        print(i ,":",count)
        