'''215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
# nums = [3,2,1,5,6,4]
# k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4


for _ in range(k):
    max_index = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i

    ans = nums[max_index]
    nums[max_index] = float('-inf')   # mark as removed

print(ans)

