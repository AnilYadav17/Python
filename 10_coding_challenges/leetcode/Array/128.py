class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        nums_list=[]
        for i in range(len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    break
                elif  nums[i]+1 == nums[i+1]:
                    nums_list.append(nums[i])

        return len(nums_list)
    

nums = [0,3,7,2,5,8,4,6,0,1]
s = Solution()
print(s.longestConsecutive(nums))