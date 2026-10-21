'''46. Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]'''



nums = [1,2,3]


result = []

for i in range(len(nums)):
	current=list(nums[i])
	
	remaining=[]
	for  j in nums:
		if j != current:
			remaining.append(j)

	print(current+remaining)


# Note: Incomplete implementation attempt (requires backtracking)
# TODO: Implement full permutations using itertools or backtracking recursion