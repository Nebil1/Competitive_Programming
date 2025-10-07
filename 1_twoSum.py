# brute force solution

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 elif target == (nums[i] + nums[j]):
#                     return [i, j]

# Two pass Hash table

# class Solution:
#     def def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map ={}
#         # 1st pass to build the mapping
#         for i in range(len(nums)):
#             hash_map[nums[i]] = i
#         # 2nd pass to check for complement
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hash_map and hash_map[complement] != i:
#                 return [i, hash_map[complement]]

# One pass Hash solution -> First build a map of numbers → then check for complements

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [seen[complement], i]
            seen[num] = i
        return []
