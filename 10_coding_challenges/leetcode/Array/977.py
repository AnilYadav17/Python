'''977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''


class Solution(object):
    def sortedSquares(self, nums):
        y = map(lambda x:x**2 ,nums)
        return sorted(y)


nums = [-4,-1,0,3,10]
s1 = Solution()
print(s1.sortedSquares(nums))