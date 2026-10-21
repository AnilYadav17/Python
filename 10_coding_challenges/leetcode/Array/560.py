'''560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

# class Solution(object):
#     def subarraySum(self, nums, k):
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 sub = nums[i:j+1]
#                 if sum(sub) == k:
#                     count += 1
#         return count
    
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            total=0
            for j in range(i, len(nums)):
                total+=nums[j]
                if total==k:
                    count+=1
                    
        return count

nums = [1,2,3]
k = 3
s1 = Solution()
print(s1.subarraySum(nums,k))