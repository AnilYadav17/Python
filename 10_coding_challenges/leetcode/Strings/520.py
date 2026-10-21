'''520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 
Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
'''
class Solution(object):
    def detectCapitalUse(self, word):
        i=0
        flag=False
        count=0
        while i<len(word):
            if word[i]>='A' and word[i]<="Z":
                count+=1
            i+=1

        if count==0 or count==len(word):
            flag=True

        if count==1:
            if word[0]>='A' and word[0]<='Z':
                flag=True

        return flag
    
    
word = "USA"
word = "FlaG"
s1 = Solution()
print(s1.detectCapitalUse(word))