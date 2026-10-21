'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
 

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 '''
class Solution(object):
    def moveZeroes(self, nums):
        #return sorted(nums,reverse=True)


        with_zero = []
        without_zero = []
        for i in nums:
            if i!=0:
                without_zero.append(i)
            else:
                with_zero.append(i)
        return without_zero+with_zero
    







        # count = nums.count(0)
        # nums = [0, 1, 0, 3, 12]
        # nums[:] = list(filter(lambda x: x != 0, nums))
        # nums.extend([0] * count)
        # return nums
    
nums = [0,1,0,3,12]
s1 = Solution()
print(s1.moveZeroes(nums))