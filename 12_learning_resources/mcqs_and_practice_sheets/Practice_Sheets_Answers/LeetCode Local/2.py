'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]'''



s =  "catsanddog"
wordDict  = ["cat","cats","and","sand","dog"]

for i in range(len(s)):
	for j in range(i+1,len(s)):
		sub = s[i:j+1]
		if sub in wordDict:
			print(sub)
