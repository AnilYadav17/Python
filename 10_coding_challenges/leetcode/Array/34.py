'''34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        ans=[]
        start=-1
        end=-1
        for i in range(len(nums)):
            if nums[i] == target:
                start=i
                break
        for i in range(len(nums)-1,start-1,-1):
            if nums[i] == target:
                end=i
                break
        return [start,end]
        

nums = [5,7,7,8,8,10]
target = 8
s1 = Solution()
print(s1.searchRange(nums,target))