'''58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        return len(s[-1])

s = "lufffffy is still joyboy"  
s1 = Solution()
print(s1.lengthOfLastWord(s))