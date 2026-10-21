'''Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

def singleNumber( nums):
        for i in nums:
            if nums.count(i)!=3 and i!=1:
                return i
            elif i==1 and nums.count(i)==1:
                return 1
        


nums = [1,0,1,0,1,0,99]
print(singleNumber(nums))
