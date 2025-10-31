# Daily coding practice - 2025_10_31 152755
# Valid Parentheses - Check if string has valid parentheses

# Solution:
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack
