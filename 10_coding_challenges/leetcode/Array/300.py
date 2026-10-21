'''300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.
 
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 '''

class Solution(object):
    def lengthOfLIS(self, nums):
        l = []
        i = 0 
        while i < len(nums):
            maxs=[]
            for j in range(i,len(nums)):
                if len(maxs) == 0:
                    maxs.append(nums[j])
                else:
                    if nums[j] > maxs[-1]:
                        maxs.append(nums[j])
            l.append(len(maxs))
            i+=1
        return max(l)
    


nums = [10,9,2,5,3,7,101,18]
s1 = Solution()
print(s1.lengthOfLIS(nums))