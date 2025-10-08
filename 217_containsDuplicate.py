# first attempt
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         count = {}
#         for i, num in enumerate(nums):
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1 
#         for i in count:
#             if count[i] >= 2:
#                 return True
#         return False

# more optimal solution
# if num already in seen return true
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return 
        
# improve runtime
# If any duplicates existed, the set will be smaller than the original list.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))