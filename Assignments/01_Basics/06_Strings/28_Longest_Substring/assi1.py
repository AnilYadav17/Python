'''1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc'''

s = input("Enter String: ")
result = ""

for i in s:
    found = 0

    for j in result:
        if i == j:
            found = 1
            break

    if found == 0:
        result += i

print(result)