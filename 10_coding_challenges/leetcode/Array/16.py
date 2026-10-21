'''16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).'''

nums = [-1,2,1,-4]
target = 1

class Solution(object):
    def threeSumClosest(self, nums, target):
        ans=[]
        triplets =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        triplet = sorted([nums[i],nums[j],nums[k]])
                        triplets.append(triplet)
        d = sum(triplets[0])-target
        for i in triplets:
            if i not in ans:
                if sum(i)-target<=d:
                    ans.append(i)
                    d=sum(i)-target
        return ans
        
################################## INCOMPLETE #######################################


s1 = Solution()
print(s1.threeSumClosest(nums,target))