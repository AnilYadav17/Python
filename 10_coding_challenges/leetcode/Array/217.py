'''217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

'''

# class Solution(object):
#     def containsDuplicate(self, nums):
#         i=0
#         d=dict()
#         while len(nums)>i:
#             d[nums[i]]=nums.count(nums[i])
#             i+=1
#         if len(d)==len(nums):
#             return False
#         else:
#             return True

# 
class Solution(object):
    def containsDuplicate(self, nums):
        i=0
        result = False
        while len(nums)>i:
            if nums.count(nums[i])>1:
                result =  True
                break
            i+=1
        return result
    


####  return len(nums) != len(set(nums))    #######
nums = [1,2,2]
s1 = Solution()
print(s1.containsDuplicate(nums))