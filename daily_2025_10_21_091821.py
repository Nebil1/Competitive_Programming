# Daily coding practice - 2025_10_21 091821
# Two Sum - Find indices of two numbers that add up to target

# Solution:
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
