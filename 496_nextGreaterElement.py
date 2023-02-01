class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ans = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            d[num] = i
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                top = stack.pop()
                if top in d:
                    ans[d[top]] = num
            stack.append(num)
        return ans
