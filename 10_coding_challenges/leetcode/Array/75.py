'''75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]'''


class Solution(object):
    def sortColors(self, nums):
        ans=[]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        # return nums

        count0=0
        count1=0
        count2=0
        ans=[]
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1

        for _ in  range(count0):
            ans.append(0)
        for _ in  range(count1):
            ans.append(1)
        for _ in  range(count2):
            ans.append(2)
        
        return ans
nums = [2,0 ,1,0,1]
s1 = Solution()
print(s1.sortColors(nums))