# Daily coding practice - 2025_10_10 084814
# Reverse String - Reverse string in-place

# Solution:
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
