class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"