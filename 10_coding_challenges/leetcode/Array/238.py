'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''


class Solution(object):
    def productExceptSelf(self, nums):
        ans=[]

        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product*=nums[j]
                
            ans.append(product)
        
        return ans



# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
s1 = Solution()
print(s1.productExceptSelf(nums))