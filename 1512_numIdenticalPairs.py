class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       freq = [0] * 102
       count = 0
       for i in nums:
           freq[i] += 1
       for i in freq:
           count += (i * (i - 1)) // 2
       return count