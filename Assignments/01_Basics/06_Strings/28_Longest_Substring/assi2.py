'''2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india'''

s = input("Enter Sentence: ").lower()

words = s.split()

max = 0
max_word = ""

for i in words:
    count = 0

    for j in words:
        if i == j:
            count += 1

    if count > max:
        max = count
        max_word = i

print("Most Frequent Word:", max_word)