'''28. Find the Index of the First Occurrence in a String
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''


class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            match = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match=False
                    break

            if match:
                return(i)
        else:
            return(-1)
                

haystack = "sabutsad"
needle = "sad"
s1 = Solution()
print(s1.strStr(haystack,needle))