'''557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
'''


s = "Mr Ding"

class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        result=[]
        for i in s:
            result.append(i[::-1])
        
        return " ".join(result)
    

s1 = Solution()
print(s1.reverseWords(s))