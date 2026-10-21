# print(ord('A'),ord('Z'))

# words =["fl","fleek","fleep","fleeeer"]

# first_word = words[0]
# result=""

# for i in range(len(first_word)):
#     match=True
#     for word in words:
#         if i >= len(word) or word[i] != first_word[i]:
#                 match=False
#                 break
#     if match:
#          result+=first_word[i]
#     else:
#          break        

# print(result)


class Solution(object):
    def topKFrequent(self, nums, k):
        result = []
        d = dict()
        for i in nums:
            if i not in d:
                d[nums.count(i)] = i
            else:
                d[nums.count(i)] += 1

        return d 


s1 = Solution()
nums = [1,1,2,3,4]
print(s1.topKFrequent(nums,2))

