class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = 0
        while (3**a<=n):
            if (3**a==n):
                return True
            a+=1
        return False