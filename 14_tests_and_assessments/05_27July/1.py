'''Problem:1 Find the Longest Substring That Appears at Both Ends(4 marks)

Problem Statement Given a string S, find the longest substring that
appears both as a prefix (beginning) and as a suffix (ending) of the
string.

The prefix and suffix must not be equal to the entire string itself. If
multiple such substrings exist, return the longest one. If no such
substring exists, print “Not Found”.

Note: The prefix and suffix may overlap.

Input Format - A single line containing the string S.

Output Format - Print the longest substring that appears as both a
prefix and a suffix. - If no such substring exists, print: Not Found

Constraints 1 ≤ |S| ≤ 100000 S consists of lowercase English letters
only.

Examples

1)  Input: ababcab Output: ab
2)  Input: level Output: l
3)  Input: abcabc Output: abc
4)  Input: abcdef Output: Not Found
5)  Input: aaaa Output: aaa

Sample Test Cases
1)  Input: banana Output: Not Found
2)  Input: abcdabc Output: abc
3)  Input: xyzxyz Output: xyz
4)  Input: ababab Output: abab
6)  Input: a Output: Not Found
7)  Input: aaaaaa Output: aaaaa
8)  Input: racecar Output: r
9)  Input: abababab Output: ababab
10) Input: abcab Output: ab
'''

s = input("Enter Substring: ")
