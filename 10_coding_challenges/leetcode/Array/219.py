'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 '''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
            if len(nums)!=1:
                start=0
                end=0
                for i in range(len(nums)-1,-1,-1):
                    if nums[i]==k:
                        start = i
                        break
                
                c=0
                for i in range(len(nums)-1,-1,-1):
                    if nums[i]==k and c>=1:
                        end = i
                        c+=1
                    if c==2:
                        break
                
                if c==0:
                    end=start

                if abs(start - end) <= k:
                    return True
                else:
                    return False
            else:
                return False

# nums = [1]
# k = 1

nums = [1,0,1,1]
k = 1
s1 = Solution()
print(s1.containsNearbyDuplicate(nums,k))