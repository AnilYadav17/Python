'''1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

Input: abcabcbb
Output: abc'''


s = input("Enter String: ")
ans = ""

for i in range(len(s)):
    temp = ""

    for j in range(i, len(s)):
        temp += s[j]

print(temp)