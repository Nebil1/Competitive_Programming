class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans