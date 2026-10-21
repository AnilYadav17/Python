'''581. Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.


Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_nums=sorted(nums)
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start=i
                break

        for i in range(len(nums)-1,-1,-1):
            if nums[i] != sorted_nums[i]:
                end=i
                break

        if start==-1 and end==-1:
            return 0
        else:
            return end-start+1
        
nums = [2,6,4,8,10,9,15]
s1 = Solution()
print(s1.findUnsortedSubarray(nums))