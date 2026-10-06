'''4. Program should work for both uppercase and lowercase letters.

 Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input: Python is very easy to learn

Output: is'''

s1 = input("Enter String: ")

lst1 = s1.split()

short = lst1[0]

for i in lst1:
    if len(i) < len(short):
        short = i

print("Shortest word is:", short)
