class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        def cmp(x, y):
            if x+y > y+x:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int("".join(nums)))