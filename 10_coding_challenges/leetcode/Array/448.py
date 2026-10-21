class Solution(object):
    def findDisappearedNumbers(self, nums):
        result=[]
        
        i=1
        while i<=len(nums):
            if i not in nums:
                result.append(i)
        return result


nums = [4,3,2,7,8,2,3,1]
s1 = Solution()
print(s1.findDisappearedNumbers(nums))