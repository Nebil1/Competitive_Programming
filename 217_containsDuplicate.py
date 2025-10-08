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

# more efficient solutions 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False